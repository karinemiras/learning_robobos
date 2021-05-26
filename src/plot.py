import glob
import numpy as np
import pickle
import pprint
import pandas as pd
import matplotlib.pyplot as plt
import sys
import seaborn as sb
from statannot import add_stat_annotation
from itertools import combinations


pd.set_option("display.max_rows", 99999)


class PlotData:

    def __init__(self, anal, experiments):
        self.anal = anal
        self.experiments =  experiments

        self.dir = 'experiments/old/'
        self.measures = ['steps', 'duration', 'total_success', 'rewards', 'step_success']
        self.measures = ['step_success']
        self.measures_limits = [[70, 150], [5, 13], [-1.5, 9.5], [-10, 80], [-10, 130]]
        self.metrics = ['max', 'mean', 'min', 'median']

    def lines(self):

        full_data_agreg = pd.read_csv(f'{self.dir}full_data_agreg.csv')
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

                plt.savefig(f'{self.dir}{self.anal}_{measure}_{metric}.png')

                # add marker max, bigger letters, better titles and axis, better colors, legends


    def boxes(self):

        plt.clf()

        tests_combinations = list(combinations(self.experiments, 2))

        full_data_agreg = pd.read_csv(f'{self.dir}full_data.csv')
        full_data_agreg = full_data_agreg[full_data_agreg['experiment'].isin(self.experiments)]

        full_data_agreg=full_data_agreg[full_data_agreg['episode'] == full_data_agreg["episode"].max()]

        print(full_data_agreg)

        for idx_measure, measure in enumerate(self.measures):
            sb.set()

            plot=sb.boxplot(x='experiment', y=measure, data=full_data_agreg) # hue='Style',

            # remove bonferroni correction?
            add_stat_annotation(plot, data=full_data_agreg, x='experiment', y=measure,# order=order,
                                box_pairs=tests_combinations,
                                test='Wilcoxon', text_format='star', loc='inside', verbose=2)

            plt.title(self.anal)
            plot.get_figure().savefig(f'{self.dir}{self.anal}_{measure}_box.png')
            plt.clf()


analysis = {
     'env1': ['env1TD3e0', 'env1TD3l1']#, 'env1TD3l5'],
    # 'env2': ['env2TD3e0', 'env2TD3l1', 'env2TD3l5'],
    # 'env3': ['env3TD3e0', 'env3TD3l1', 'env3TD3l5']
}

# analysis = {
#     'eng': ["env1112TD3l1", "env111TD3l1"]
#
# }





for anal in analysis:
    cd = PlotData(anal, analysis[anal])
   # cd.lines()
    cd.boxes()








