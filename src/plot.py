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

        print(experiments)

        self.dir = 'experiments/'
        #self.measures = ['steps', 'duration', 'total_success', 'rewards', 'step_success']
        self.measures = ['steps', 'total_success', 'rewards', 'step_success']
        #self.measures_limits = [[70, 150], [5, 13], [-1.5, 9.5], [-10, 80], [-10, 130]]
        self.measures_limits = [[70, 150], [-1.5, 9.5], [-10, 80], [-10, 130]]
        self.metrics = ['max', 'mean', 'min', 'median']
        self.clrs = ['#CC0000', '#006600']

        plt.style.use('classic')

    def lines(self):

        full_data_agreg = pd.read_csv(f'{self.dir}{self.anal}_full_data_agreg.csv')
        full_data_agreg =  full_data_agreg[full_data_agreg['experiment'].isin(self.experiments)]

        print(full_data_agreg)

        for idx_measure, measure in enumerate(self.measures):

            for metric in self.metrics:
                fig, ax = plt.subplots()

                for idx_experiment, experiment in enumerate(self.experiments):

                    data = full_data_agreg[full_data_agreg['experiment'] == experiment]

                    ax.plot(data['episode'], data[f'{measure}_{metric}'], label=experiment, c=self.clrs[idx_experiment])

                    if metric == 'median':
                        ax.fill_between(data['episode'],
                                         data[f'{measure}_q25'],
                                         data[f'{measure}_q75'],
                                        alpha=0.3, facecolor=self.clrs[idx_experiment])

                    if metric == 'mean':
                        ax.fill_between(data['episode'],
                                        data[f'{measure}_{metric}'] - data[f'{measure}_std'],
                                        data[f'{measure}_{metric}'] + data[f'{measure}_std'],
                                        alpha=0.3 , facecolor=self.clrs[idx_experiment])

                    ax.set_ylim((self.measures_limits[idx_measure][0], self.measures_limits[idx_measure][1]))
                    plt.xlabel('Stage')
                    plt.ylabel(f'{measure}_{metric}')
                    plt.title(self.anal)
                    ax.legend()

                plt.grid()
                plt.savefig(f'{self.dir}{self.anal}_{measure}_{metric}.png')

                # add marker max, bigger letters, better titles and axis, better colors, legends


    def boxes(self):

        plt.clf()

        tests_combinations = list(combinations(self.experiments, 2))

        full_data_agreg = pd.read_csv(f'{self.dir}{self.anal}_full_data.csv')
        full_data_agreg = full_data_agreg[full_data_agreg['experiment'].isin(self.experiments)]

        full_data_agreg = full_data_agreg[full_data_agreg['episode'] == full_data_agreg["episode"].max()]

        print(full_data_agreg)

        for idx_measure, measure in enumerate(self.measures):
            sb.set()
            sb.set_style("whitegrid")

            plot=sb.boxplot(x='experiment', y=measure, data=full_data_agreg, palette=self.clrs) # hue='Style',

            #remove bonferroni correction?
            if len(tests_combinations) > 0:
                add_stat_annotation(plot, data=full_data_agreg, x='experiment', y=measure,# order=order,
                                    box_pairs=tests_combinations,
                                    test='Wilcoxon', text_format='star', loc='inside', verbose=2)

            plt.title(self.anal)
            plot.get_figure().savefig(f'{self.dir}{self.anal}_{measure}_box.png')
            plt.clf()

analysis = {
     'for_seen_TD':  ["for_seen_TD"],
     'for_mseen_TD': ["for_mseen_TD"],
}


for anal in analysis:
    cd = PlotData(anal, analysis[anal])
    cd.lines()
    cd.boxes()








