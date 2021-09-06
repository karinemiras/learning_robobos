import glob
import pickle
import pprint
import os
import time
import traceback

from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3 import TD3
from stable_baselines3.common.callbacks import BaseCallback

from info_log import Log


class CustomCallback(BaseCallback):
    """
    A custom callback that derives from ``BaseCallback``.

    :param verbose: (int) Verbosity level 0: not output 1: info 2: debug
    """
    def __init__(self, experiment_manager=None,  verbose=1):
        super(CustomCallback, self).__init__(verbose)
        # Those variables will be accessible in the callback
        # (they are defined in the base class)
        # The RL model
        # self.model = None  # type: BaseRLModel
        # An alias for self.model.get_env(), the environment used for training
        # self.training_env = None  # type: Union[gym.Env, VecEnv, None]
        # Number of time the callback was called
        # self.n_calls = 0  # type: int
        # self.num_timesteps = 0  # type: int
        # local and global variables
        # self.locals = None  # type: Dict[str, Any]
        # self.globals = None  # type: Dict[str, Any]
        # The logger object, used to report things in the terminal
        # self.logger = None  # type: logger.Logger
        # # Sometimes, for event callback, it is useful
        # # to have access to the parent object
        # self.parent = None  # type: Optional[BaseCallback]

        self.experiment_manager = experiment_manager

    def _on_training_start(self) -> None:
        """
        This method is called before the first rollout starts.
        """
        pass

    def _on_rollout_start(self) -> None:
        """
        A rollout is the collection of environment interaction
        using the current policy.
        This event is triggered before collecting new samples.
        """
        pass

    def _on_step(self) -> bool:
        """
        This method will be called by the model after each call to `env.step()`.

        For child callback (of an `EventCallback`), this will be called
        when the event is triggered.

        :return: (bool) If the callback returns False, training is aborted early.
        """

        # if human is interfering, adds actions to replay
        if len(self.experiment_manager.env.human_actions) > 0:
            self.experiment_manager.model.replay_buffer.add(
                        self.experiment_manager.env.human_actions[0],
                        self.experiment_manager.env.human_actions[1],
                        self.experiment_manager.env.human_actions[2],
                        self.experiment_manager.env.human_actions[3],
                        self.experiment_manager.env.human_actions[4]
                 )

        self.validate_policy()
        self.save_checkpoint()

        return True

    def _on_rollout_end(self) -> None:
        """
        This event is triggered before updating the policy.
        """
        pass

    def _on_training_end(self) -> None:
        """
        This event is triggered before exiting the `learn()` method.
        """
        pass

    def validate_policy(self):
        if self.num_timesteps % self.experiment_manager.config.validation_freq == 0:
            print('> Validating...')

            for i in range(1, self.experiment_manager.config.number_validations+1):
                print(' validation', i)
                self.experiment_manager.mode_train_validation = 'validation'
                obs = self.experiment_manager.env.reset()
                done = False
                while not done:
                    action, _states = self.experiment_manager.model.predict(obs)
                    obs, rewards, done, info = self.experiment_manager.env.step(action)

                self.experiment_manager.mode_train_validation = 'train'

            print(' ')

    def save_checkpoint(self):
        if self.num_timesteps % self.experiment_manager.config.checkpoint_timesteps == 0:

            self.experiment_manager.current_checkpoint += 1
            self.experiment_manager.save_checkpoint()
            self.experiment_manager.log.write(f'SAVED checkpoint {self.experiment_manager.current_checkpoint}', True)


class ExperimentManager:

    def __init__(self,
                 config,
                 model,
                 environment,
                 load,
                 log_food_print=False):

        self.config = config
        self.model = model
        self.env = environment
        self.load = load
        self.log_food_print = log_food_print
        self.env.exp_manager = self
        self.log = Log(self.config.experiment_name)

        self.results_episodes = []
        self.results_episodes_validation = []
        self.current_checkpoint = 0
        self.current_episode = 0
        self.mode_train_validation = 'train'

    def register_episode(self):
        if self.mode_train_validation == 'train':
            self.current_episode += 1

    def register_step(self, rewards):

        if self.mode_train_validation == 'train':
            self.results_episodes.append([
                                        self.current_episode,
                                        self.env.current_step,
                                        self.env.total_success,
                                        self.env.total_hurt,
                                        rewards])
        else:
            self.results_episodes_validation.append([
                                        self.current_episode,
                                        self.env.current_step,
                                        self.env.total_success,
                                        self.env.total_hurt,
                                        rewards])


    def food_print(self):
        if self.mode_train_validation == 'train':
            print(f'food in episode  {self.current_episode}: {self.env.total_success}  hurt: {self.env.total_hurt} steps: {self.env.current_step}')
        else:
            print(f'   food: {self.env.total_success} hurt: {self.env.total_hurt} steps: {self.env.current_step}')

        if self.log_food_print:
            file = open(f'experiments/final_tests.txt', 'a')
            file.write(f'{self.config.experiment_name}\t{self.config.sim_hard}\t{self.env.total_success}\t{self.env.total_hurt}\t {self.env.current_step}\n')
            file.close()

    def run(self):

        # loads checkpoint if existent, or prepares new stage
        self.prepare_stage()

        callback = CustomCallback(experiment_manager=self)

        self.log.write(f'STARTING checkpoint {self.current_checkpoint+1}')

        try:

            remaining_training_timesteps = self.config.training_timesteps-len(self.results_episodes)
            self.model.learn(total_timesteps=remaining_training_timesteps,
                             log_interval=5, #in episodes
                             callback=callback)
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
                     self.results_episodes_validation,
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
                    self.results_episodes, self.results_episodes_validation, self.current_checkpoint, self.current_episode = pickle.load(f)
                    #
                    # if self.config.human_interference:
                    #     env2 = self.env
                    # else:
                        # only recovers pickle if model also available
                    env2 = DummyVecEnv([lambda: self.env])

                    self.model = self.load(f'{dir}/model_checkpoint_{checkpoints[attempts]}', env=env2)

                    attempts = -1

                    self.log.write(f'RECOVERED checkpoint {checkpoints[attempts]}')

                except:
                    self.log.write(f'ERROR: Could not recover checkpoint {checkpoints[attempts]}  {traceback.format_exc()}')
                    self.results_episodes, self.results_episodes_validation, self.current_checkpoint, self.current_episode = [], [], 0, 0

                attempts -= 1

    def test_policy(self, experiment, run, checkpoint):

        self.load_stage(checkpoint)

        print('> Testing ', experiment, run)
        for i in range(1, self.config.number_tests+1):
            print('  Test', i)
            obs = self.env.reset()
            done = False
            while not done:
                action, _states = self.model.predict(obs)
                obs, rewards, done, info = self.env.step(action)


    #TODO: reuse this function in preparestage later
    def load_stage(self, checkpoint):
        dir = f'experiments/{self.config.experiment_name}'
        f = open(f'{dir}/status_checkpoint_{checkpoint}.pkl', 'rb')

        self.results_episodes, self.results_episodes_validation, self.current_checkpoint, self.current_episode = pickle.load(f)
        # only recovers pickle if model also available
        env2 = DummyVecEnv([lambda: self.env])
        self.model = self.load(f'{dir}/model_checkpoint_{checkpoint}', env=env2)


