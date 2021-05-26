import glob
import numpy as np
import pickle
import pprint
import pandas as pd
import matplotlib.pyplot as plt
import sys

pd.set_option("display.max_rows", 99999)


class ConsolidateData:

    def __init__(self,
                 experiments,
                 runs):

        self.experiments = experiments
        self.runs = runs
        self.dir = 'experiments/eng/'

    def run(self):

        full_data = pd.DataFrame()

        for experiment in self.experiments:

            for run in self.runs:

                print(experiment, run)

                measures = ['steps', 'duration', 'total_success', 'rewards']
                data = self.recover_latest_checkpoint(experiment, run)

                df = pd.DataFrame(data, columns=['episode']+measures)

                # adds index for repetitions
                df['val_index'] = df['steps']
                df['val_index'] = df.val_index.eq(1).cumsum()

                # get relevant values from each episode
                df_relevant = df.groupby(['episode', 'val_index']).agg(
                                steps=('steps', max),
                                duration=('duration', max),
                                total_success=('total_success', max),
                                rewards=('rewards', sum)
                            ).reset_index()

                # calculates earliest step of max success
                df = df.rename(columns={'steps': 'step_success'}, inplace=False)
                step_success = df.iloc[df.groupby(['episode', 'val_index'])['total_success'].
                                            agg(pd.Series.idxmax)].filter(['episode',  'val_index', 'step_success'])

                df_relevant = df_relevant.merge(step_success, on=['episode', 'val_index'])

                #  average validation episodes
                df_avg_intra = df_relevant.groupby('episode').agg(
                                steps=('steps', 'mean'),
                                duration=('duration', 'mean'),
                                total_success=('total_success', 'mean'),
                                rewards=('rewards', 'mean'),
                                step_success=('step_success', 'mean')
                            ).reset_index()
                df_avg_intra['duration'] = round(df_avg_intra['duration'] / 1000 / 60, 1)

                df_avg_intra['episode'] = range(1, len(df_avg_intra)+1)
                df_avg_intra['experiment'] = experiment
                df_avg_intra['run'] = run
                pprint.pprint(df_avg_intra)

                full_data = pd.concat([full_data, df_avg_intra])

        def q25(x):
            return x.quantile(0.25)
        def q75(x):
            return x.quantile(0.75)

        # average runs
        full_data_agreg = full_data.groupby(['experiment', 'episode'])\
                                .agg(
                                    steps_median=('steps', 'median'),
                                    steps_mean=('steps', 'mean'),
                                    steps_std=('steps', 'std'),
                                    steps_max=('steps', 'max'),
                                    steps_min=('steps', 'min'),
                                    steps_q25=('steps', q25),
                                    steps_q75=('steps', q75),
                                    duration_median=('duration', 'median'),
                                    duration_mean=('duration', 'mean'),
                                    duration_std=('duration', 'std'),
                                    duration_max=('duration', 'max'),
                                    duration_min=('duration', 'min'),
                                    duration_q25=('duration', q25),
                                    duration_q75=('duration', q75),
                                    total_success_median=('total_success', 'median'),
                                    total_success_mean=('total_success', 'mean'),
                                    total_success_std=('total_success', 'std'),
                                    total_success_max=('total_success', 'max'),
                                    total_success_min=('total_success', 'min'),
                                    total_success_q25=('total_success', q25),
                                    total_success_q75=('total_success', q75),
                                    rewards_median=('rewards', 'median'),
                                    rewards_mean=('rewards', 'mean'),
                                    rewards_std=('rewards', 'std'),
                                    rewards_max=('rewards', 'max'),
                                    rewards_min=('rewards', 'min'),
                                    rewards_q25=('rewards', q25),
                                    rewards_q75=('rewards', q75),
                                    step_success_median=('step_success', 'median'),
                                    step_success_mean=('step_success', 'mean'),
                                    step_success_std=('step_success', 'std'),
                                    step_success_max=('step_success', 'max'),
                                    step_success_min=('step_success', 'min'),
                                    step_success_q25=('step_success', q25),
                                    step_success_q75=('step_success', q75)
                                    ).reset_index()


        full_data_agreg.to_csv(f'{self.dir}full_data_agreg.csv')
        full_data.to_csv(f'{self.dir}full_data.csv')


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
                return results_episodes_validation
            except:
                print(f'ERROR: Could not recover checkpoint {checkpoints[attempts]} {traceback.format_exc()}')
            attempts -= 1


cd = ConsolidateData(
        experiments=[
                     # "env1TD3e0",
                     # "env1TD3l1",
                     # "env1TD3l5",
                     # "env2TD3e0",
                     # "env2TD3l1",
                     # "env2TD3l5",
                     # "env3TD3e0",
                     # "env3TD3l1",
                     # "env3TD3l5"
    "env1112TD3l1", "env111TD3l1"
                     ],
        runs=range(1, 10+1)
)

cd.run()








