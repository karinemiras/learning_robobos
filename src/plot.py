import glob
import numpy as np
import pickle
import pprint
import pandas as pd
import matplotlib.pyplot as plt
import sys

pd.set_option("display.max_rows", 99999)


class PlotData:

    def __init__(self, anal, experiments):
        self.anal = anal
        self.experiments =  experiments

        self.dir = 'experiments/new_env_greenmile_rand/'
        self.measures = ['steps', 'duration', 'total_success', 'rewards', 'step_success']
        self.measures_limits = [[1,1 ], [1,1 ], [-1.5, 9.5], [1,1 ], [1,1]]
        self.metrics = ['max', 'mean', 'min', 'median']

    def run(self):

        full_data_agreg = pd.read_csv(f'{self.dir}consolidated.csv')
        full_data_agreg =  full_data_agreg[full_data_agreg['experiment'].isin(self.experiments)]

        print(full_data_agreg)

        for idx_measure, measure in enumerate(self.measures):

            for metric in self.metrics:
                fig, ax = plt.subplots()

                for experiment in self.experiments:

                    data = full_data_agreg[full_data_agreg['experiment'] == experiment]

                    ax.plot(data['episode'], data[f'{measure}_{metric}'], label=experiment)#, c=clrs[i])

                    if metric == 'median':
                        ax.fill_between(data['episode'],
                                         data[f'{measure}_q25'],
                                         data[f'{measure}_q75'],
                                        alpha=0.3)#, facecolor=clrs[i])

                    if metric == 'mean':
                        ax.fill_between(data['episode'],
                                        data[f'{measure}_{metric}'] - data[f'{measure}_std'],
                                        data[f'{measure}_{metric}'] + data[f'{measure}_std'],
                                        alpha=0.3)  # , facecolor=clrs[i])

                    ax.set_ylim((self.measures_limits[idx_measure][0], self.measures_limits[idx_measure][1]))
                    plt.xlabel('Stage')
                    plt.ylabel(f'{measure}_{metric}')
                    plt.title(self.anal)
                    ax.legend()

                plt.savefig(f'{self.dir}{measure}_{metric}.png')

                # add marker max, bigger letters, better titles and axis, better colors, legends



#
# analysis = {
#     'env1': ['env1TD3e0', 'env1TD3l1', 'env1TD3l5'],
#     'env2': ['env2TD3e0', 'env2TD3l1', 'env2TD3l5'],
#     'env3': ['env3TD3e0', 'env3TD3l1', 'env3TD3l5']
# }


analysis = {
    'test': ['forageTD3e0', 'forageTD3l1', 'forageTD3l5']
}

for anal in analysis:
    cd = PlotData(anal, analysis[anal])
    cd.run()








