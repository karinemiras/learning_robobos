#!/usr/bin/env python3
from __future__ import print_function

import numpy as np
import gym
from gym import spaces
from stable_baselines.td3.policies import MlpPolicy

from stable_baselines import TD3
from stable_baselines.ddpg.noise import NormalActionNoise, OrnsteinUhlenbeckActionNoise
import os
import robobo
from numpy import inf
import cv2
import time
from scipy.spatial import KDTree
from webcolors import (
    css3_hex_to_names,
    hex_to_rgb,
)


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
        self.max_millis = 2000
        self.min_left = -3
        self.max_left = 3
        self.min_right = -3
        self.max_right = 3
        self.max_food = 7

        # pan: positive is left. 600 looks back fully.
        # tilted: positive is back. 300 looks up almost fully.
        self.min_tilt = 0
        self.max_tilt = -50
        self.min_pan = -600
        self.max_pan = 600

        self.episode_length = 150000 #200000

        #shorter?

        # init
        self.done = False
        self.accumulated_food = 0
        self.start_time = 0
        self.previous_state = np.array([0,0])

        # Define action and observation space
        self.action_space = spaces.Box(low=0, high=1,
                                       shape=(2,), dtype=np.float32)
        # why high and low?
        self.observation_space = spaces.Box(low=0, high=1,
                                            shape=(5,), dtype=np.float32)


        self.env = robobo.SimulationRobobo().connect(address='192.168.0.100', port=19997)

    def reset(self):
        print('food',self.accumulated_food)
        #counts steps here!
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

        self.env.set_phone_tilt(-100)

        # randomize position
        observations = self.get_infrared()
        color_y, color_x = self.detect_color()
        observations = np.append(observations, [color_y, color_x])

        return np.array(observations).astype(np.float32)

    def step(self, action):

        info = {}

       # print('')
        #print('action', action)

        # fetches and transforms actions

        action_left = action[0]
        action_right = action[1]
        #action_millis = action[2]

        left = action_left * (self.max_left - self.min_left) + self.min_left
        right = action_right * (self.max_right - self.min_right) + self.min_right


        # freedom_millis = self.max_millis - self.min_millis
        # millis = self.min_millis + freedom_millis * action_millis


        #print('action transf',left, right, millis, pan, tilt)

        # performs actions

        self.env.move(left, right)#, millis)

        # gets states

        observations = self.get_infrared()

        sim_time = self.env.get_sim_time()


        color_y, color_x = self.detect_color()

        #print('duration', millis)
        #print(observations.astype(np.float32))

        collected_food = self.env.collected_food()
        if sim_time - self.start_time >= self.episode_length or collected_food == self.max_food:
            self.done = True

        # calculates rewards

        if collected_food - self.accumulated_food > 0:
            food_reward = 10
        else:
            food_reward = 0

        self.accumulated_food = self.env.collected_food()


        if color_y and color_x:
            sight = 0.1
        else:
            sight = 0

        observations = np.append(observations, [color_y, color_x])

        reward = food_reward + sight

        #print(observations, 'food ' ,food_reward,  ' sight ',sight)

        return observations.astype(np.float32), reward, self.done, info

    def render(self, mode='console'):
        pass

    def close(self):
        pass

    def get_infrared(self):

        irs = np.asarray(self.env.read_irs()).astype(np.float32)

        irs[irs != 0] = 1

        back = max(irs[0], irs[1], irs[2])
        front1 = max(irs[3], irs[4], irs[5])
        front2 = max(irs[5], irs[6], irs[7])

        observations = [back, front1, front2]

        return observations

    def detect_color(self):

        image = self.env.get_image_front()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        ## mask of green
        mask = cv2.inRange(hsv, (36, 25, 25), (70, 255, 255))

        if cv2.countNonZero(mask) > 0:
            y = np.where(mask == 255)[0]
            x = np.where(mask == 255)[1]
            avg_y = sum(y) / len(y)
            avg_x = sum(x) / len(x)

        else:
            avg_x = 0
            avg_y = 0

        # test = 1 if avg_x and avg_y else 0
        # sim_time = self.env.get_sim_time()
        # cv2.imwrite(str(sim_time) + str(test)+ '.png', image)
        #

        return avg_y, avg_x

    def convert_rgb_to_names(self, rgb_tuple):
        # a dictionary of all the hex and their respective names in css3
        css3_db = css3_hex_to_names
        names = []
        rgb_values = []
        for color_hex, color_name in css3_db.items():
            names.append(color_name)
            rgb_values.append(hex_to_rgb(color_hex))

        kdt_db = KDTree(rgb_values)
        distance, index = kdt_db.query(rgb_tuple)
        return names[index]


env = RoboboEnv()


#check if models exists and loads it to resume training



#noise? smaller step train?

n_actions = env.action_space.shape[-1]
action_noise = NormalActionNoise(mean=np.zeros(n_actions), sigma=0.1 * np.ones(n_actions))


start = 1
# withcolor_slower_1 (not fully 200)
# withcolor_slower_2

name = 'withcolor_slower_3'

i = start

while i<= 10:

    print("=====stage =====", i)

    if i == 1:

        model = TD3(MlpPolicy, env, action_noise=action_noise, verbose=1)
    else:
        print('load')
        env2 = DummyVecEnv([lambda: env])
        model = TD3.load(name, env=env2)

        try:
            model.learn(total_timesteps=5000)
            model.save(name)
            i += 1
        except Exception as error:
            print('ERROR loop: {}'.format(error))



#########
model = TD3.load(name)
print('TESTE')
for i in range(0, 5):
    obs = env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)


