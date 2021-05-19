import os
os.environ["KMP_WARNINGS"] = "FALSE"

from config import Config
from experiment_manager import ExperimentManager
from foraging_env import ForagingEnv

config = Config()
config = config.parser.parse_args()
config.robot_port = 20000
config.train_or_test = 'test'
foraging_env = ForagingEnv(config=config)

experiments = [
    #"forageTD3e0"#,
    #"forageTD3e1",
    #"forageTD3e2",
    "forageTD3l1"#,
   # "forageTD3l5"
]

runs = 1
save_results = True

for experiment in experiments:
    for run in range(1, runs+1):

        config.experiment_name = f'{experiment}_{run}'
        print('\n'+config.experiment_name)
        em = ExperimentManager(config=config,
                               model=None,
                               environment=foraging_env).test_policy(save_results, experiment, run)

#  ./coppeliaSim.sh -h scenes/robobo_food_arena.ttt  -gREMOTEAPISERVERSERVICE_26666_FALSE_TRUE
