#!/usr/bin/env python3
from __future__ import print_function

import numpy as np
import gym
from gym import spaces
from stable_baselines.td3.policies import MlpPolicy
from stable_baselines import TD3
import os
import robobo
from numpy import inf
import cv2
import time

# does this matter!?
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

class RoboboEnv(gym.Env):
    """
    Custom gym Environment.
    """

    # ham?!
    # Because of google colab, we cannot implement the GUI ('human' render mode)
    metadata = {'render.modes': ['console']}

    def __init__(self):
        super(RoboboEnv, self).__init__()

        # params
        self.min_millis = 500
        self.max_millis = 1000
        self.min_left = -1
        self.max_left = 1
        self.min_right = -1
        self.max_right = 1
        # pan: positive is left. 600 looks back fully.
        # tilted: positive is back. 300 looks up almost fully.
        self.min_tilt = 0
        self.max_tilt = -50
        self.min_pan = -600
        self.max_pan = 600

        self.episode_length = 50000

        # init
        self.done = False
        self.accumulated_food = 0
        self.start_time = 0

        # Define action and observation space
        self.action_space = spaces.Box(low=0, high=1,
                                       shape=(5,), dtype=np.float32)
        # why high and low?
        self.observation_space = spaces.Box(low=-1, high=1,
                                            shape=(9,), dtype=np.float32)


        self.env = robobo.SimulationRobobo().connect(address='192.168.0.100', port=19997)

    def reset(self):
        print('food',self.accumulated_food)
        """
        Important: the observation must be a numpy array
        :return: (np.array)
        """
        self.done = False
        self.accumulated_food = 0

        self.env.stop_world()
        while self.env.is_simulation_running():
            pass

        self.env.play_simulation()
        while self.env.is_simulation_stopped():
            pass

        self.start_time = self.env.get_sim_time()

        observations = self.get_infrared()
        bloob = self.detect_bloob()
        observations = np.append(observations, [bloob])

        return np.array(observations).astype(np.float32)

    def step(self, action):

        info = {}

        #print('')
        print('action', action)

        # fetches and transforms actions

        action_left = action[0]
        action_right = action[1]
        action_millis = action[2]
        action_pan = action[3]
        action_tilt = action[4]

        # finds x's from the normalization z = (x-min)/(max-min), where z's are the action's
        pan = action_pan * (self.max_pan-self.min_pan) + self.min_pan
        tilt = action_tilt * (self.max_tilt - self.min_tilt) + self.min_tilt

        # somehow rotations only work properly with multiples of 50
        pan = int(round(pan / 50) * 50)
        tilt = int(round(tilt / 50) * 50)

        left = action_left * (self.max_left - self.min_left) + self.min_left
        right = action_right * (self.max_right - self.min_right) + self.min_right


        # left = self.max_left * action_left
        # right = self.max_right * action_right
        freedom_millis = self.max_millis - self.min_millis
        millis = self.min_millis + freedom_millis * action_millis


        print('action transf',left, right, millis, pan, tilt)

        # performs actions

        # use pan?
        #self.env.set_phone_pan(pan, self.speed_pan_tilt)
        self.env.set_phone_tilt(tilt)
        self.env.move(left*5, right*5, millis)

        # gets states

        observations = self.get_infrared()

        sim_time = self.env.get_sim_time()


        bloob = self.detect_bloob()
        observations = np.append(observations, [bloob])
        #print('duration', millis)
        #print(observations.astype(np.float32))

        if sim_time - self.start_time >= self.episode_length:
            self.done = True

        # calculates rewards

        if self.env.collected_food() - self.accumulated_food > 0:
            food_reward = 2
        else:
            food_reward = 0

        self.accumulated_food = self.env.collected_food()
        touch_penalty = np.sum(observations)
        if abs(touch_penalty) > 0:
            if bloob == 0:
                touch_penalty = -1
        else:
            touch_penalty = 0

        reward = food_reward + touch_penalty + bloob
        #print('total ',reward, 'food ' ,food_reward, 'touch ',touch_penalty, ' sight ',bloob)

        return observations.astype(np.float32), reward, self.done, info

    def render(self, mode='console'):
        pass

    def close(self):
        pass

    def get_infrared(self):

        # TODO: make differerent transf?
        irs = np.array(self.env.read_irs())
        observations = np.log(irs) / 10
        observations[observations == -inf] = 0

        return observations

    def detect_bloob(self):

        image = self.env.get_image_front()

        # print(image)
        detector = cv2.SimpleBlobDetector_create()
        keypoints = detector.detect(image)

        if len(keypoints) > 0:
            # print('===blooob======',keypoints)
            bloob = 1
            # cv2.imwrite('bloob_'+str(sim_time) + '.png', image)
            # im_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255),
            #                                       cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            # cv2.imwrite('bloob_'+str(sim_time) + '.png', im_with_keypoints)
        else:
            bloob = 0
            # cv2.imwrite(str(sim_time) + '.png', image)

        return bloob


env = RoboboEnv()


# #check if models exists and loads it to resume training
# env2 = DummyVecEnv([lambda: env])
# model = TD3.load("evosave_td3", env=env2)
#

model = TD3(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=500000)
model.save("test1")



#########
# model = TD3.load("test1")
#
# for i in range(0, 4):
#     obs = env.reset()
#     env.env.speed = 'normal'
#     done = False
#     while not done:
#         action, _states = model.predict(obs)
#         obs, rewards, done, info = env.step(action)
#
#
