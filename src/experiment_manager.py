import pickle
import pprint

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

        # try to load checkpoitns here

        while self.current_checkpoint < self.config.checkpoints:

            self.current_checkpoint += 1

            self.log.write(f'STARTING checkpoint {self.current_checkpoint}')

            try:
                self.model.learn(total_timesteps=self.config.checkpoint_timesteps,
                             log_interval=10)
            except Exception as error:
                self.log.write(f'ERROR loop: {error}')

            self.log.write(f'FINISHED checkpoint {self.current_checkpoint}')

            self.save_checkpoint()

            self.log.write(f'SAVED checkpoint {self.current_checkpoint}')


    def save_checkpoint(self):

        self.model.save(f'checkpoint_{self.current_checkpoint}')

        #f = open(f'{folder}/individuals/individual_{self.id}.pkl', "wb")
        f = open(f'checkpoint_{self.current_checkpoint}.pkl', "wb")
        pickle.dump([self.results_episodes,
                     self.current_checkpoint,
                     self.current_episode], f)

#pprint.pprint(experiment.results_episodes)



# load checkpoint / fix exps name / if no checkpoint /if over