import glob
import pickle
import pprint
import os
import time
import traceback

from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import TD3

from info_log import Log


class ExperimentManager:

    def __init__(self,
                 config,
                 model,
                 environment):

        self.config = config
        self.model = model
        self.env = environment
        self.env.exp_manager = self
        self.log = Log(self.config.experiment_name)

        self.results_episodes = []
        self.current_checkpoint = 0
        self.current_episode = 0


    def register_episode(self):
        self.current_episode += 1

    def register_step(self, rewards):
        self.results_episodes.append([
                                    self.current_episode,
                                    self.env.current_step,
                                    self.env.finish_time,
                                    self.env.total_success,
                                    rewards])

    def run(self):

        # loads checkpoint if existent, or prepares new stage
        self.prepare_stage()

        # runs each stage of training
        while self.current_checkpoint < self.config.checkpoints:

            self.log.write(f'STARTING checkpoint {self.current_checkpoint+1}')

            try:
                self.model.learn(total_timesteps=self.config.checkpoint_timesteps,
                                 log_interval=10)

                self.current_checkpoint += 1

                self.log.write(f'FINISHED checkpoint {self.current_checkpoint}')

                self.save_checkpoint()

                self.log.write(f'SAVED checkpoint {self.current_checkpoint}', True)

            except Exception as error:
                self.log.write(f'ERROR: {traceback.format_exc()}')

                time.sleep(1)

        self.env.robot.stop_world()

    def save_checkpoint(self):

        dir = f'experiments/{self.config.experiment_name}'

        self.model.save(f'{dir}/model_checkpoint_{self.current_checkpoint}')

        f = open(f'{dir}/status_checkpoint_{self.current_checkpoint}.pkl', 'wb')
        pickle.dump([
                     self.results_episodes,
                     self.current_checkpoint,
                     self.current_episode
                     ], f)

    def prepare_stage(self):

        dir = f'experiments/{self.config.experiment_name}'
        if not os.path.exists(dir):
            os.mkdir(dir)

        else:

            # recovers the latest non-corrupted checkpoint, if existent

            checkpoints = []
            for file in glob.glob(f'{dir}/status_checkpoint*'):
                checkpoints.append(int(file.split('/status_checkpoint_')[1].split('.')[0]))
                checkpoints.sort()

            attempts = len(checkpoints)-1

            while attempts >= 0:
                try:
                    f = open(f'{dir}/status_checkpoint_{checkpoints[attempts]}.pkl', 'rb')
                    self.results_episodes, self.current_checkpoint, self.current_episode = pickle.load(f)

                    # only recovers pickle if model also available
                    env2 = DummyVecEnv([lambda: self.env])
                    self.model = TD3.load(f'{dir}/model_checkpoint_{checkpoints[attempts]}', env=env2)

                    attempts = -1

                    self.log.write(f'RECOVERED checkpoint {checkpoints[attempts]}')

                except:
                    self.log.write(f'ERROR: Could not recover checkpoint {checkpoints[attempts]}')
                    self.results_episodes, self.current_checkpoint, self.current_episode = [], 0, 0

                attempts -= 1

