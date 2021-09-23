from config import Config
from experiment_manager import ExperimentManager

from TD3_loop import TD3_loop


config = Config()
config = config.parser.parse_args()

if config.task == 'foraging':
    from foraging import ForagingEnv
    env = ForagingEnv(config=config)


def load(dir1, dir2, env, config):
    td = TD3_loop(env, config)
    td.load(dir1, dir2)
    return td


model = TD3_loop(env, config)

ExperimentManager(config=config,
                  model=model,
                  environment=env,
                  load=load
                  ).run()
