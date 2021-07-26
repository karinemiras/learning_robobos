import numpy as np
import os
os.environ["KMP_WARNINGS"] = "FALSE"

os.environ['CUDA_VISIBLE_DEVICES'] = '1'


from config import Config
from experiment_manager import ExperimentManager
from foraging_mseen import ForagingEnv

from stable_baselines3 import TD3
from stable_baselines3.td3.policies import MlpPolicy
from stable_baselines3.common.noise import NormalActionNoise


config = Config()
config = config.parser.parse_args()

foraging_env = ForagingEnv(config=config)

n_actions = foraging_env.action_space.shape[-1]
action_noise = NormalActionNoise(mean=np.zeros(n_actions),
                                 sigma=0.1 * np.ones(n_actions))

def load(name, env):
    return TD3.load(name, env)

model = TD3(MlpPolicy,
            foraging_env,
            action_noise=action_noise,
            learning_rate=0.0003,
            verbose=1)

ExperimentManager(config=config,
                  model=model,
                  environment=foraging_env,
                  load=load
                  ).run()
