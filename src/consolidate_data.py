import glob
import numpy as np
import pickle
import pprint
import pandas as pd


class ConsolidateData:

    def __init__(self,
                 experiments):

        self.experiments = experiments
        self.dir = 'experiments/'
        self.aggregation_episodes = 10

    def run(self):

        for experiment in self.experiments:
            data = self.recover_latest_checkpoint(experiment)

            pd.set_option("display.max_rows", 9999)

            measures = ['steps', 'duration', 'total_success', 'rewards']
            measures_limits = [[100,130], [160, 210], [0, 7], [5, 80]]

            df = pd.DataFrame(data, columns=['episode']+measures)

            df_agreg = df.groupby('episode').agg(
                            steps=('steps', max),
                            duration=('duration', max),
                            total_success=('total_success', max),
                            rewards=('rewards', sum)
                        )



            df_agreg['duration'] = df_agreg['duration']/1000

            df =  df.rename(columns={'steps': 'step_success'}, inplace=False)
            step_success = df.iloc[df.groupby('episode')['total_success'].
                                        agg(pd.Series.idxmax)].filter(['episode', 'step_success'])

            df_agreg = df_agreg.merge(step_success, on='episode')

            df_agreg['episode'] = (df_agreg['episode']/self.aggregation_episodes)+1
            df_agreg = df_agreg.astype({'episode': int})

            df_agreg = df_agreg.groupby('episode').agg(
                steps=('steps', np.mean),
                duration=('duration', np.mean),
                total_success=('total_success', np.mean),
                rewards=('rewards', np.mean),
                step_success=('step_success', np.mean)
            ).reset_index()

            # TODO: what is wrong with steps?
            # temp hack!
           # df_agreg = df_agreg[df_agreg['episode'] < 17]
            pprint.pprint(df_agreg)

            for idx, measure in enumerate(measures):
                plot = df_agreg.plot.line(x='episode', y=measure)
                plot.set_ylim(measures_limits[idx][0], measures_limits[idx][1])
                plot.get_figure().savefig(f'{self.dir}{experiment}/{measure}.png')

    def recover_latest_checkpoint(self, experiment_name):
        dir = f'{self.dir}{experiment_name}'
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
        experiments=['default_experiment1',
                     'default_experiment2']
)

cd.run()








