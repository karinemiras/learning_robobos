#!/usr/bin/env python3
from __future__ import print_function

import cv2
import gym
from gym import spaces
import numpy as np
import os
import time

import robobo

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
        self.current_step = 0
        self.start_time = None
        self.finish_time = None
        self.exp_manager = None

        if self.config.train_or_test == 'train':
            self.episode_length = self.config.episode_train_time
        else:
            self.episode_length = self.config.episode_test_time

        # Define action and sensors space
        self.action_space = spaces.Box(low=0, high=1,
                                       shape=(2,), dtype=np.float32)
        # why high and low?
        self.observation_space = spaces.Box(low=0, high=1,
                                            shape=(5,), dtype=np.float32)

        self.robot = robobo.SimulationRobobo().connect(address=self.config.robot_ip, port=self.config.robot_port)
        time.sleep(1)

    def reset(self):

        """
        Important: the observation must be a numpy array
        :return: (np.array)
        """

        print('food',self.total_success)

        self.exp_manager.register_episode()

        self.done = False
        self.total_success = 0
        self.current_step = 0

        self.robot.stop_world()
        while self.robot.is_simulation_running():
            pass

        self.robot.play_simulation()
        while self.robot.is_simulation_stopped():
            pass

        self.robot.set_phone_tilt(-100)

        self.start_time = self.robot.get_sim_time()

        # TODO: randomize position

        sensors = self.get_infrared()
        color_y, color_x = self.detect_color()
        sensors = np.append(sensors, [color_y, color_x])

        return np.array(sensors).astype(np.float32)

    def step(self, actions):

        info = {}

        # fetches and transforms actions

        action_left = actions[0]
        action_right = actions[1]
        #action_millis = actions[2]

        left = action_left * (self.config.max_left - self.config.min_left) + self.config.min_left
        right = action_right * (self.config.max_right - self.config.min_right) + self.config.min_right

        #freedom_millis = self.config.max_millis - self.config.min_millis
        #millis = self.config.min_millis + freedom_millis * action_millis

        # performs actions

        #self.robot.move(left, right, millis)
        self.robot.move(left, right)

        # gets states

        self.finish_time = self.robot.get_sim_time()

        sensors = self.get_infrared()

        color_y, color_x = self.detect_color()

        collected_food = self.robot.collected_food()
        if self.finish_time - self.start_time >= self.episode_length or collected_food == self.max_food:
            self.done = True

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

        #print(sensors, 'actions 'actions)
        #print(sensors, 'food ' ,food_reward,  ' sight ',sight)

        self.current_step += 1

        self.exp_manager.register_step(food_reward+sight)

        return sensors.astype(np.float32), reward, self.done, info

    def render(self, mode='console'):
        pass

    def close(self):
        pass

    def get_infrared(self):

        irs = np.asarray(self.robot.read_irs()).astype(np.float32)

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
        mask = cv2.inRange(hsv, (36, 25, 25), (70, 255, 255))

        if cv2.countNonZero(mask) > 0:
            y = np.where(mask == 255)[0]
            x = np.where(mask == 255)[1]
            avg_y = sum(y) / len(y)
            avg_x = sum(x) / len(x)

        else:
            avg_y = 0
            avg_x = 0

        # if green detected, returns average positions of y and x
        return avg_y, avg_x
