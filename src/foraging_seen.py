#!/usr/bin/env python3
from __future__ import print_function

import cv2
import gym
from gym import spaces
import numpy as np
import os
import time

import robobo
from action_selection import ActionSelection

# TODO: fix this?
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


class ForagingEnv(gym.Env):
    """
    Custom gym Environment.
    """
    metadata = {'render.modes': ['console']}

    def __init__(self, config):

        super(ForagingEnv, self).__init__()

        # params

        self.config = config

        self.max_food = 7
        self.food_reward = 10
        self.sight_reward = 0.1

        # init
        self.done = False
        self.total_success = 0
        self.total_hurt = 0
        self.current_step = 0
        self.exp_manager = None

        # Define action and sensors space
        self.action_space = spaces.Box(low=0, high=1,
                                       shape=(4,), dtype=np.float32)
        # why high and low?
        self.observation_space = spaces.Box(low=0, high=1,
                                            shape=(5,), dtype=np.float32)

        self.action_selection = ActionSelection(self.config)

        self.robot = False
        while not self.robot:
            if self.config.sim_hard == 'sim':
                self.robot = robobo.SimulationRobobo().connect(address=self.config.robot_ip, port=self.config.robot_port)
            else:
                self.robot = robobo.HardwareRobobo(camera=True).connect(address=self.config.robot_ip_hard)

            time.sleep(1)

    def reset(self):

        """
        Important: the observation must be a numpy array
        :return: (np.array)
        """

        self.done = False
        self.total_success = 0
        self.current_step = 0

        self.exp_manager.register_episode()

        if self.config.sim_hard == 'sim':
            self.robot.stop_world()
            while self.robot.is_simulation_running():
                pass

            self.robot.set_position()

            self.robot.play_simulation()
            while self.robot.is_simulation_stopped():
                pass

        # TODO: fix correct values
        if self.config.sim_hard == 'sim':
            self.robot.set_phone_tilt(-100)
        else:
            self.robot.set_phone_tilt(92)

        sensors = self.get_infrared()
        color_y, color_x = self.detect_color()
        sensors = np.append(sensors, [color_y, color_x])

        return np.array(sensors).astype(np.float32)

    def step(self, actions):

        info = {}

        # fetches and transforms actions
        left, right, millis, apply_reward = self.action_selection.select(actions)

        self.robot.move(left, right, millis)

        # gets states
        sensors = self.get_infrared()
        color_y, color_x = self.detect_color()

        if self.config.sim_hard == 'sim':
            collected_food, aux = self.robot.collected_food()
        else:
            collected_food = 0

        if self.exp_manager.config.train_or_test == 'train':
            # train
            if self.exp_manager.mode_train_validation == 'train':
                episode_length = self.config.episode_train_steps
            # validation
            else:
                episode_length = self.config.episode_validation_steps
        else:
            # final test
            episode_length = self.config.episode_test_steps

        # calculates rewards

        if collected_food - self.total_success > 0:
            food_reward = self.food_reward
        else:
            food_reward = 0

        self.total_success = collected_food

        if color_y and color_x:
            sight = self.sight_reward
        else:
            sight = -self.sight_reward

        sensors = np.append(sensors, [color_y, color_x])

        reward = food_reward + sight

        if self.config.human_interference:
            if reward > 0:
                reward = reward * apply_reward

        # if episode is over
        if self.current_step == episode_length-1 or collected_food == self.max_food:
            self.done = True
            self.food_print()

        self.current_step += 1

        self.exp_manager.register_step(reward)

        return sensors.astype(np.float32), reward, self.done, info

    def render(self, mode='console'):
        pass

    def food_print(self):
        if self.exp_manager.mode_train_validation == 'train':
            print(f'food in episode {self.exp_manager.current_episode}: {self.total_success}')
        else:
            print(f'   food: {self.total_success}')

    def close(self):
        pass

    def get_infrared(self):

        irs = np.asarray(self.robot.read_irs()).astype(np.float32)

        #np.set_printoptions(suppress=True)
        if self.config.sim_hard == 'hard':
            # sets threshold for sensors ghosts : change to lambda later
            for idx, val in np.ndenumerate(irs):
                if irs[idx] >= 100:
                    irs[idx] = 1
                else:
                    irs[idx] = 0
        #print('a',irs)

        irs[irs != 0] = 1

        back   = max(irs[0], irs[1], irs[2])
        front1 = max(irs[3], irs[4], irs[5])
        front2 = max(irs[5], irs[6], irs[7])

        sensors = [back, front1, front2]

        return sensors

    def detect_color(self):

        image = self.robot.get_image_front()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # mask of green
        mask = cv2.inRange(hsv, (45, 70, 70), (85, 255, 255))

        #cv2.imwrite("imgs/" + str(self.current_step)+ "mask.png", mask)
        #cv2.imwrite("imgs/" + str(self.current_step) + "img.png", image)

        size_y = len(image)
        size_x = len(image[0])

        if cv2.countNonZero(mask) > 0:
            y = np.where(mask == 255)[0]
            x = np.where(mask == 255)[1]

            # average positions normalized by image size
            avg_y = sum(y) / len(y) / (size_y - 1)
            avg_x = sum(x) / len(x) / (size_x - 1)

        else:
            avg_y = 0
            avg_x = 0

        return avg_y, avg_x

