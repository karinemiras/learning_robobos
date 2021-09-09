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
        self.human_penalty = -1

        # init
        self.done = False
        self.human_actions = []
        self.total_success = 0
        self.total_hurt = 0
        self.current_step = 0
        self.exp_manager = None
        self.episode_length = 0
        self.previous_sensors = None

        # Define action and sensors space
        self.action_space = spaces.Box(low=0, high=1,
                                       shape=(3,), dtype=np.float32)

        # why high and low?
        self.observation_space = spaces.Box(low=0, high=1,
                                            shape=(7,), dtype=np.float32)

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

        if self.config.sim_hard == 'sim':
            self.robot.set_phone_tilt(-100)
        else:
            self.robot.set_phone_tilt(92)

        pos_x = self.normalize(self.robot.position()[0], 'x')
        pos_y = self.normalize(self.robot.position()[1], 'y')

        sensors = self.get_infrared()
        color_y, color_x = self.detect_color()
        sensors = np.append(sensors, [color_y, color_x, pos_x, pos_y])
        sensors = np.array(sensors).astype(np.float32)

        self.previous_sensors = sensors

        return sensors

    def step(self, actions):

        info = {}

        # fetches and transforms actions
        left, right, prop_diff, human_actions = self.action_selection.select(actions)

        self.robot.move(left, right, 500)

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
                self.episode_length = self.config.episode_train_steps
            # validation
            else:
                self.episode_length = self.config.episode_validation_steps
        else:
            # final test
            self.episode_length = self.config.episode_test_steps

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

        pos_x = self.normalize(self.robot.position()[0], 'x')
        pos_y = self.normalize(self.robot.position()[1], 'y')

        sensors = np.append(sensors, [color_y, color_x, pos_x, pos_y])

        reward = food_reward + sight

        human_reward = 0
        if self.config.human_interference and prop_diff > 0:
               human_reward = reward
               if human_reward > 0:
                   human_reward *= 100
               else:
                   human_reward = 0
               reward = -reward * prop_diff

        # if episode is over
        if self.current_step == self.episode_length-1 or collected_food == self.max_food:
            self.done = True
            self.exp_manager.food_print()

        self.current_step += 1

        self.exp_manager.register_step(reward)

        sensors = sensors.astype(np.float32)

        human_actions = [self.previous_sensors, sensors, np.array(human_actions), np.array(human_reward), np.array(self.done)]
        self.human_actions = human_actions

        self.previous_sensors = sensors

        return sensors, reward, self.done, info

    def render(self, mode='console'):
        pass

    def close(self):
        pass

    def normalize(self, var, axis):
        max = 1
        min = 0

        if axis == 'x':
            old_min = -4.08
            old_max = -2.16
        else:
            old_min = -0.16
            old_max = 1.76

        old_range = old_max - old_min
        new_range = max - min
        var = (var - old_min) / old_range * new_range + min
        return var

    def get_infrared(self):

        irs = np.asarray(self.robot.read_irs()).astype(np.float32)

        if self.config.sim_hard == 'hard':
            # sets threshold for sensors ghosts : change to lambda later
            for idx, val in np.ndenumerate(irs):
                if irs[idx] >= 100:
                    irs[idx] = 1
                else:
                    irs[idx] = 0

        irs[irs != 0] = 1

        back   = max(irs[0], irs[1], irs[2])
        front1 = max(irs[3], irs[4], irs[5])
        front2 = max(irs[5], irs[6], irs[7])

        sensors = [back, front1, front2]

        return sensors

    def detect_color(self):

        image = self.robot.get_image_front()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        #cv2.imshow('grayscale image', image)

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

