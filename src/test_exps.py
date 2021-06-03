import os
os.environ["KMP_WARNINGS"] = "FALSE"

from config import Config
from experiment_manager import ExperimentManager
from foraging_env_seen import ForagingEnv

config = Config()
config = config.parser.parse_args()
config.robot_port = 19997 #20020
config.train_or_test = 'test'
foraging_env = ForagingEnv(config=config)

experiments = [
    "envseenTD3l3"
]

runs = [20]
save_results = True

for experiment in experiments:
    for run in runs:

        config.experiment_name = f'{experiment}_{run}'
        print('\n'+config.experiment_name)
        em = ExperimentManager(config=config,
                               model=None,
                               environment=foraging_env).test_policy(experiment, run)

#  xvfb-run ./coppeliaSim.sh -h scenes/robobo_food_arena.ttt  -gREMOTEAPISERVERSERVICE_20020_FALSE_TRUE
