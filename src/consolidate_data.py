import glob
import numpy as np
import pickle
import pprint
import pandas as pd
import matplotlib.pyplot as plt
import sys
import traceback

pd.set_option("display.max_rows", 99999)


class ConsolidateData:

    def __init__(self,
                 experiment,
                 runs):

        self.experiment = experiment
        self.runs = runs
        self.dir = 'experiments/'

    def run(self):

        full_data = pd.DataFrame()

        print(f' ---------{self.experiment}---------')

        for run in self.runs:

            print(self.experiment, run)

            measures = ['steps', 'total_success', 'total_hurt', 'rewards']
            data = self.recover_latest_checkpoint(experiment, run)

            df = pd.DataFrame(data, columns=['episode']+measures)

            # adds index for repetitions
            df['val_index'] = df['steps']
            df['val_index'] = df.val_index.eq(1).cumsum()

            # get relevant values from each episode
            df_relevant = df.groupby(['episode', 'val_index']).agg(
                            steps=('steps', max),
                            total_success=('total_success', max),
                            rewards=('rewards', sum)
                        ).reset_index()

            #  average validation episodes
            df_avg_intra = df_relevant.groupby('episode').agg(
                            steps=('steps', 'mean'),
                            total_success=('total_success', 'mean'),
                            rewards=('rewards', 'mean')
                        ).reset_index()

            df_avg_intra['episode'] = range(1, len(df_avg_intra)+1)
            df_avg_intra['experiment'] = experiment
            df_avg_intra['run'] = run

            pprint.pprint(df_avg_intra)

            full_data = pd.concat([full_data, df_avg_intra])

        full_data = full_data.rename(columns={'episode': 'checkpoint'})

        # average runs
        full_data_agreg = full_data.groupby(['experiment', 'checkpoint'])\
                                .agg(
                                    steps_median=('steps', 'median'),
                                    steps_mean=('steps', 'mean'),
                                    steps_std=('steps', 'std'),
                                    steps_max=('steps', 'max'),
                                    steps_min=('steps', 'min'),
                                    steps_q25=('steps', self.q25),
                                    steps_q75=('steps', self.q75),
                                    total_success_median=('total_success', 'median'),
                                    total_success_mean=('total_success', 'mean'),
                                    total_success_std=('total_success', 'std'),
                                    total_success_max=('total_success', 'max'),
                                    total_success_min=('total_success', 'min'),
                                    total_success_q25=('total_success', self.q25),
                                    total_success_q75=('total_success', self.q75),
                                    total_hurt_median=('total_success', 'median'),
                                    rewards_median=('rewards', 'median'),
                                    rewards_mean=('rewards', 'mean'),
                                    rewards_std=('rewards', 'std'),
                                    rewards_max=('rewards', 'max'),
                                    rewards_min=('rewards', 'min'),
                                    rewards_q25=('rewards', self.q25),
                                    rewards_q75=('rewards', self.q75)
                                    ).reset_index()

        full_data_agreg.to_csv(f'{self.dir}anal/{self.experiment}_full_data_agreg.csv')
        full_data.to_csv(f'{self.dir}anal/{self.experiment}_full_data.csv')

    def recover_latest_checkpoint(self, experiment_name, run):
        dir = f'{self.dir}{experiment_name}_{run}'
        checkpoints = []
        for file in glob.glob(f'{dir}/status_checkpoint*'):
            checkpoints.append(int(file.split('/status_checkpoint_')[1].split('.')[0]))
            checkpoints.sort()

        attempts = len(checkpoints) - 1
        while attempts >= 0:
            try:
                f = open(f'{dir}/status_checkpoint_{checkpoints[attempts]}.pkl', 'rb')
                env_data = pickle.load(f)
                if len(env_data) > 4:
                    results_episodes, results_episodes_validation, dummy1, dummy2, human_steps = env_data
                else:
                    results_episodes, results_episodes_validation, dummy1, dummy2 = env_data

                return results_episodes_validation
            except:
                print(f'ERROR: Could not recover checkpoint {checkpoints[attempts]} {traceback.format_exc()}')
            attempts -= 1

    def q25(self, x):
        return x.quantile(0.25)

    def q75(self, x):
        return x.quantile(0.75)


#experiments = ["foraging-TD", "h_foraging-TD"]
experiments = ["ih_foraging-TD"]

for experiment in experiments:
    cd = ConsolidateData(
            experiment=experiment,
            runs=range(1, 21+1)
    )

    cd.run()

