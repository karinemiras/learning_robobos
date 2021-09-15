import numpy as np

from TD3.utils import ReplayBuffer
from TD3.TD3 import TD3
import os
os.environ["KMP_WARNINGS"] = "FALSE"
os.environ['CUDA_VISIBLE_DEVICES'] = '1'

class TD3_loop:

	def __init__(self, environment):
		self.env = environment
		self.policy = None

		self.max_timesteps = 0  # Max time steps to run environment
		self.start_timesteps = 0   			 # Time steps initial random policy is used
		self.expl_noise = 0.1     			 # Std of Gaussian exploration noise
		self.batch_size = 128      			 # Batch size for both actor and critic
		self.policy_noise = 0.2				 # Noise added to target policy during critic update
		self.noise_clip = 0.5  				 # Range to clip target policy noise
		self.policy_freq = 2 				 # Frequency of delayed policy updates

		self.init_policy()

	def init_policy(self):
		self.state_dim = self.env.observation_space.shape[0]
		self.action_dim = self.env.action_space.shape[0]
		self.max_action = float(self.env.action_space.high[0])

		kwargs = {
			"state_dim": self.state_dim,
			"action_dim": self.action_dim,
			"max_action": self.max_action,
		}

		# Target policy smoothing is scaled wrt the action scale
		kwargs["policy_noise"] = self.policy_noise * self.max_action
		kwargs["noise_clip"] = self.noise_clip * self.max_action
		kwargs["policy_freq"] = self.policy_freq
		self.policy = TD3(**kwargs)

	def learn(self, total_timesteps, log_interval,  callback):

		self.max_timesteps = total_timesteps

		replay_buffer = ReplayBuffer(self.state_dim, self.action_dim)

		state, done = self.env.reset(), False
		episode_timesteps = 0

		for t in range(int(self.max_timesteps)):

			episode_timesteps += 1

			# Select action randomly or according to policy
			if t < self.start_timesteps:
				action = self.env.action_space.sample()
			else:
				action = (
					self.policy.select_action(np.array(state))
					+ np.random.normal(0, self.max_action * self.expl_noise, size=self.action_dim)
				).clip(-self.max_action, self.max_action)

			# Perform action
			next_state, reward, done, info = self.env.step(action)

			# if human interfered, uses its actions
			if len(info) != 0:
				action = info
				human_reward_base = 1
				# if human action is successful, punishes robot potential action according to magnitude of success
				if reward > 0:
					reward = human_reward_base + reward
				else:
					reward = human_reward_base
			# 	print('h',action,reward)
			# else:
			# 	print('r', action, reward)

			done_bool = float(done) if episode_timesteps < self.env.episode_length else 0

			callback.num_timesteps += 1
			callback._on_step()

			# Store data in replay buffer
			replay_buffer.add(state, action, next_state, reward, done_bool)

			state = next_state

			# Train agent after collecting sufficient data
			if t >= self.start_timesteps:
				self.policy.train(replay_buffer, self.batch_size)

			if done:
				# Reset environment
				state, done = self.env.reset(), False
				episode_timesteps = 0

	def save(self, dir):
		self.policy.save(dir)

	def load(self, dir):
		self.policy.load(dir)


