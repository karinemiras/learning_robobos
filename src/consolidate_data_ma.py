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

            measures = ['steps', 'total_success', 'total_hurt', 'rewards']
            data = self.recover_latest_checkpoint(experiment, run)

            df = pd.DataFrame(data, columns=['episode']+measures)

            # get relevant values from each episode
            df_relevant = df.groupby(['episode']).agg(
                            steps=('steps', max),
                            total_success=('total_success', max),
                            total_hurt=('total_hurt', max),
                            rewards=('rewards', sum)
                        ).reset_index()

            moving_window = 10

            for id_m, measure in enumerate(measures):
                df_relevant[measure+'_ma'] = df_relevant.iloc[:, id_m+1].rolling(window=moving_window).mean()

            df_relevant['episode'] = range(1, len(df_relevant)+1)
            df_relevant['experiment'] = experiment
            df_relevant['run'] = run

            pprint.pprint(df_relevant)
            full_data = pd.concat([full_data, df_relevant])

        full_data.to_csv(f'{self.dir}anal/{self.experiment}_full_data_ma.csv')

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
                results_episodes, results_episodes_validation, dummy1, dummy2 = pickle.load(f)
                return results_episodes
            except:
                print(f'ERROR: Could not recover checkpoint {checkpoints[attempts]} {traceback.format_exc()}')
            attempts -= 1


experiments = ["foraging-TD"]

for experiment in experiments:
    cd = ConsolidateData(
            experiment=experiment,
            runs=range(1, 20+1) 
    )

    cd.run()








