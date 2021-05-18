import glob
import numpy as np
import pickle
import pprint
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_rows", 9999)


class ConsolidateData:

    def __init__(self,
                 experiments,
                 runs):

        self.experiments = experiments
        self.runs = runs
        self.dir = 'experiments/'
        self.aggregation_episodes = 10

    def run(self):

        full_data = pd.DataFrame()

        for experiment in self.experiments:

            for run in range(1, self.runs+1):

                data = self.recover_latest_checkpoint(experiment, run)

                measures = ['steps', 'time', 'total_success', 'rewards']
                measures_limits = [[100,130], [160, 210], [0, 7], [5, 80]]

                df = pd.DataFrame(data, columns=['episode']+measures)

                df_agreg = df.groupby('episode').agg(
                                steps=('steps', max),
                                duration=('time', max),
                                total_success=('total_success', max),
                                rewards=('rewards', sum)
                            ).reset_index()

                df = df.rename(columns={'steps': 'step_success'}, inplace=False)
                step_success = df.iloc[df.groupby('episode')['total_success'].
                                            agg(pd.Series.idxmax)].filter(['episode', 'step_success'])

                df_agreg = df_agreg.merge(step_success, on='episode')

                df_agreg['experiment'] = experiment
                df_agreg['run'] = run
                full_data = pd.concat([full_data, df_agreg])

        #pprint.pprint(full_data)

        # make quartiles later
        aggregations = ['max', 'mean', 'std']
        full_data_agreg = full_data.groupby(['experiment', 'episode'])\
                                .agg(
                                    steps_mean=('steps', 'mean'),
                                    steps_max=('steps', 'max'),
                                    steps_std=('steps', 'std'),
                                    duration_mean=('duration', 'mean'),
                                    duration_max=('duration', 'max'),
                                    duration_std=('duration', 'std'),
                                    total_success_mean=('total_success', 'mean'),
                                    total_success_max=('total_success', 'max'),
                                    total_success_std=('total_success', 'std'),
                                    rewards_mean=('rewards', 'mean'),
                                    rewards_max=('rewards', 'max'),
                                    rewards_std=('rewards', 'std')
                                    ).reset_index()

        pprint.pprint(full_data_agreg)
        #print(full_data_agreg.dtypes)
       # print(full_data_agreg['total_success']['mean'])
       # for idx, measure in enumerate(measures):
        #    plot = df_agreg.plot.line(x='episode', y=measure)
            #plot.set_ylim(measures_limits[idx][0], measures_limits[idx][1])
            #plot.get_figure().savefig(f'{self.dir}{measure}.png')

        fig, ax = plt.subplots()

        for key, grp in full_data_agreg.groupby(['experiment']):
            ax = grp.plot(ax=ax, kind='line', x='episode', y='total_success_mean' , label=key) #c

        plt.legend(loc='best')
        plt.show()

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
                results_episodes, dummy1, dummy2 = pickle.load(f)
                return results_episodes
            except:
                print(f'ERROR: Could not recover checkpoint {checkpoints[attempts]}')
            attempts -= 1


cd = ConsolidateData(
        experiments=["forageTD3e0",
                     "forageTD3e1",
                    # "forageTD3e2",
                    # "forageTD3l1",
                   #  "forageTD3l5"
                     ],
        runs=15
)

cd.run()








