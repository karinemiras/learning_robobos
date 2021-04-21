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

        # Define action and observation space
        self.action_space = spaces.Box(low=0, high=1,
                                            shape=(3,), dtype=np.float32)
        # why high and low?
        self.observation_space = spaces.Box(low=-1, high=0,
                                            shape=(8,), dtype=np.float32)


        self.env = robobo.SimulationRobobo().connect(address='192.168.0.100', port=19997)
        self.env.play_simulation()

    def reset(self):
        """
        Important: the observation must be a numpy array
        :return: (np.array)
        """

        observations = np.log(np.array(self.env.read_irs())) / 10
        #print('reset',observations)
        return np.array(observations).astype(np.float32)

    def step(self, action):

        print('')
        #print('action outside', action)

        action_left = action[0]
        action_right = action[1]
        action_millis = action[2]

        info = {}

        r = 1
        done = False
        min_millis = 500
        max_millis = 3000
        max_left = 1
        max_right = 1
        freedom_millis = max_millis - min_millis

        millis = min_millis + freedom_millis * action_millis

        left = max_left * action_left
        right = max_right * action_right

       # print(left, right, millis)
        self.env.move(left, right, millis)

        #print(self.env.get_sim_time())

        irs = np.array(self.env.read_irs())
        print('antes',irs)

        # get also camera image: more reward for green in the moddle
        # ger reward from touch package
        # make rotation action?



        observations = np.log(irs) / 10

        observations[observations == -inf] = 0

        print('depois',irs)
        print(observations.astype(np.float32), r, done)
        return observations.astype(np.float32), r, done, info

    def render(self, mode='console'):
        pass

    def close(self):
        pass




env = RoboboEnv()


# #check if models exists and loads it to resume training
# env2 = DummyVecEnv([lambda: env])
# model = TD3.load("evosave_td3", env=env2)
#

model = TD3(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=150000)
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
