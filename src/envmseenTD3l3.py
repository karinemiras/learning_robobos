import numpy as np
import os
os.environ["KMP_WARNINGS"] = "FALSE"

os.environ['CUDA_VISIBLE_DEVICES'] = '1'


from config import Config
from experiment_manager import ExperimentManager
from foraging_env_mseen import ForagingEnv

from stable_baselines import TD3
from stable_baselines.td3.policies import MlpPolicy
from stable_baselines.ddpg.noise import NormalActionNoise


config = Config()
config = config.parser.parse_args()

foraging_env = ForagingEnv(config=config)

n_actions = foraging_env.action_space.shape[-1]
action_noise = NormalActionNoise(mean=np.zeros(n_actions),
                                 sigma=0.1 * np.ones(n_actions))
model = TD3(MlpPolicy,
            foraging_env,
            action_noise=action_noise,
            random_exploration=0,
            learning_rate=0.0003,
            verbose=1)

ExperimentManager(config=config,
                  model=model,
                  environment=foraging_env).run()
