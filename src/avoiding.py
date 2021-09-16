#!/usr/bin/env python3
from __future__ import print_function

import cv2
import gym
from gym import spaces
import numpy as np
import os
import time
import pprint
import math

import robobo
from action_selection_c import ActionSelection

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
        self.avoid_reward = -0.1
        self.human_reward = -1
        self.episode_length = 0

        # init
        self.done = False
        self.total_success = 0
        self.total_hurt = 0
        self.current_step = 0
        self.exp_manager = None

        # Define action and sensors space
        self.action_space = spaces.Box(low=0, high=1,
                                       shape=(3,), dtype=np.float32)
        # why high and low?
        self.observation_space = spaces.Box(low=0, high=1,
                                            shape=(17,), dtype=np.float32)

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
            self.robot.set_phone_tilt(55*math.pi/180)
        else:
            self.robot.set_phone_tilt(92)

        sensors = self.get_infrared()
        prop_green_points, color_y, color_x, prop_red_points, color_y_red, color_x_red, prop_gray_points, color_y_gray, color_x_gray = self.detect_color()
        sensors = np.append(sensors, [color_y, color_x, prop_green_points, color_y_red, color_x_red, prop_red_points, color_y_gray, color_x_gray, prop_gray_points])
        sensors = np.array(sensors).astype(np.float32)
        self.previous_sensors = sensors

        return sensors

    def step(self, actions):

        info = {}

        # fetches and transforms actions
        left, right, prop_diff, human_actions = self.action_selection.select(actions)

        self.robot.move(left, right, 250)

        # gets states
        sensors = self.get_infrared()
        prop_green_points, color_y, color_x, prop_red_points, color_y_red, color_x_red, prop_gray_points, color_y_gray, color_x_gray = self.detect_color()

        if self.config.sim_hard == 'sim':
            collected_food, collected_hurt = self.robot.collected_food()
        else:
            collected_food = 0
            collected_hurt = 0

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

        if collected_hurt - self.total_hurt > 0:
            avoid_reward = self.avoid_reward
        else:
            avoid_reward = 0

        self.total_success = collected_food
        self.total_hurt = collected_hurt

        if color_y and color_x:
            sight = self.sight_reward
        else:
            sight = -self.sight_reward

        sensors = np.append(sensors, [color_y, color_x, prop_green_points, color_y_red, color_x_red, prop_red_points, color_y_gray, color_x_gray, prop_gray_points])

        reward = food_reward + sight + avoid_reward

        # if episode is over
        if self.current_step == self.episode_length-1 or collected_food == self.max_food:
            self.done = True
            self.exp_manager.food_print()

        self.current_step += 1

        self.exp_manager.register_step(reward)

        sensors = sensors.astype(np.float32)

        info = human_actions

        return sensors, reward, self.done, info

    def render(self, mode='console'):
        pass


    def close(self):
        pass

    def get_infrared(self):

        irs = np.asarray(self.robot.read_irs()).astype(np.float32)
        if self.config.sim_hard == 'hard':
            # sets threshold for sensors ghosts : change to lambda later
            for idx, val in np.ndenumerate(irs):
                if irs[idx] >= 100:
                    irs[idx] = 1
                else:
                    irs[idx] = 0

        return irs

    def detect_color(self):

        image = self.robot.get_image_front()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # mask of green
        mask = cv2.inRange(hsv, (45, 70, 70), (85, 255, 255))
        # mask of red
        mask_red = cv2.inRange(hsv, (0, 50, 50), (10, 255, 255))
        # mask of gray
        mask_gray = cv2.inRange(hsv, (0, 0, 0), (255, 10, 255))

        size_y = len(image)
        size_x = len(image[0])

        total_points = size_y * size_x
        number_green_points = cv2.countNonZero(mask)
        prop_green_points = number_green_points / total_points

        number_red_points = cv2.countNonZero(mask_red)
        prop_red_points = number_red_points / total_points

        number_gray_points = cv2.countNonZero(mask_gray)
        prop_gray_points = number_gray_points / total_points

        if cv2.countNonZero(mask) > 0:
            y = np.where(mask == 255)[0]
            x = np.where(mask == 255)[1]
            # average positions normalized by image size
            avg_y = sum(y) / len(y) / (size_y - 1)
            avg_x = sum(x) / len(x) / (size_x - 1)
        else:
            avg_y = 0
            avg_x = 0

        if cv2.countNonZero(mask_red) > 0:
            y_red = np.where(mask_red == 255)[0]
            x_red = np.where(mask_red == 255)[1]
            avg_y_red = sum(y_red) / len(y_red) / (size_y - 1)
            avg_x_red = sum(x_red) / len(x_red) / (size_x - 1)

        else:
            avg_y_red = 0
            avg_x_red = 0

        if cv2.countNonZero(mask_gray) > 0:
            y_gray = np.where(mask_gray == 255)[0]
            x_gray = np.where(mask_gray == 255)[1]

            # average positions normalized by image size
            avg_y_gray = sum(y_gray) / len(y_gray) / (size_y - 1)
            avg_x_gray = sum(x_gray) / len(x_gray) / (size_x - 1)
        else:
            avg_y_gray = 0
            avg_x_gray = 0

        return prop_green_points, avg_y, avg_x, prop_red_points, avg_y_red, avg_x_red, prop_gray_points, avg_y_gray, avg_x_gray

