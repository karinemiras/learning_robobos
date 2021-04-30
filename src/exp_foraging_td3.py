import numpy as np

from config import Config
from experiment_manager import ExperimentManager
from foraging_env import ForagingEnv

from stable_baselines import TD3
from stable_baselines.td3.policies import MlpPolicy
from stable_baselines.ddpg.noise import NormalActionNoise, OrnsteinUhlenbeckActionNoise


config = Config()
config = config.parser.parse_args()

foraging_env = ForagingEnv(config=config)

n_actions = foraging_env.action_space.shape[-1]
action_noise = NormalActionNoise(mean=np.zeros(n_actions),
                                 sigma=0.1 * np.ones(n_actions))
model = TD3(MlpPolicy,
            foraging_env,
            action_noise=action_noise,
            verbose=1)

ExperimentManager(config=config,
                  model=model,
                  environment=foraging_env).run()