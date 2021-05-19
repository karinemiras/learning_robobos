#!/usr/bin/env python3
from __future__ import print_function

import cv2
import gym
from gym import spaces
import numpy as np
import os
import time
import random

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
        self.sight_reward = -0.1

        # init
        self.done = False
        self.total_success = 0
        self.current_step = 0
        self.duration = 0
        self.start_time = None
        self.exp_manager = None

        # Define action and sensors space
        self.action_space = spaces.Box(low=0, high=1,
                                       shape=(2,), dtype=np.float32)
        # why high and low?
        self.observation_space = spaces.Box(low=0, high=1,
                                            shape=(6,), dtype=np.float32)

        self.robot = False
        while not self.robot:
            self.robot = robobo.SimulationRobobo().connect(address=self.config.robot_ip, port=self.config.robot_port)
            time.sleep(1)

    def reset(self):

        """
        Important: the observation must be a numpy array
        :return: (np.array)
        """

        self.done = False
        self.total_success = 0
        self.current_step = 0
        self.duration = 0

        self.exp_manager.register_episode()

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
        prop_green_points, color_y, color_x = self.detect_color()
        sensors = np.append(sensors, [prop_green_points, color_y, color_x])

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
        sensors = self.get_infrared()
        prop_green_points, color_y, color_x = self.detect_color()
        collected_food = self.robot.collected_food()

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

        if prop_green_points > 0:
            sight = prop_green_points
        else:
            sight = self.sight_reward

        sensors = np.append(sensors, [prop_green_points, color_y, color_x])

        reward = food_reward + sight

       # print(sensors, 'actions 'actions)
        #print(sensors, 'food ' ,food_reward,  ' sight ',sight)

        # if episode is over
        if self.current_step == episode_length-1 or collected_food == self.max_food:
            self.done = True
            self.duration = self.robot.get_sim_time() - self.start_time
            self.food_print()

        self.current_step += 1

        self.exp_manager.register_step(food_reward+sight)

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
        number_green_points = cv2.countNonZero(mask)
        total_points = 16384 #128*128
        prop_green_points = number_green_points/total_points
        #cv2.imwrite(str(random.randint(0, 100000))+"_"+str(prop_green_points)+".png", image)

        if number_green_points > 0:
            y = np.where(mask == 255)[0]
            x = np.where(mask == 255)[1]
            avg_y = sum(y) / len(y)
            avg_x = sum(x) / len(x)

        else:
            avg_y = 0
            avg_x = 0

        # if green detected, returns proportion of green points and average positions of y and x
        return prop_green_points, avg_y, avg_x

