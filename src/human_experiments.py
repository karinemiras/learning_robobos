from config import Config
from experiment_manager import ExperimentManager

from TD3_loop import TD3_loop


config = Config()
config = config.parser.parse_args()

if config.task == 'foraging':
    from foraging import ForagingEnv

if config.task == 'avoiding':
    from avoiding import ForagingEnv


env = ForagingEnv(config=config)


def load(dir, env):
    td = TD3_loop(env)
    td.load(dir)
    return td


model = TD3_loop(env)

ExperimentManager(config=config,
                  model=model,
                  environment=env,
                  load=load
                  ).run()
