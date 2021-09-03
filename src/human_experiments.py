from config import Config
from experiment_manager import ExperimentManager

from TD3_loop import TD3_loop


config = Config()
config = config.parser.parse_args()

if config.environment == 'foraging_seen':
    from foraging_seen import ForagingEnv

if config.environment == 'foraging_mseen':
    from foraging_mseen import ForagingEnv

if config.environment == 'avoiding_mseen':
    from avoiding_mseen import ForagingEnv

if config.environment == 'avoiding_seen':
    from avoiding_seen import ForagingEnv


foraging_env = ForagingEnv(config=config)


def load(dir, env):
    td = TD3_loop(env)
    td.load(dir)
    return td


model = TD3_loop(foraging_env)

ExperimentManager(config=config,
                  model=model,
                  environment=foraging_env,
                  load=load
                  ).run()
