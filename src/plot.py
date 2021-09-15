import pprint
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from statannot import add_stat_annotation
from itertools import combinations
import sys

pd.set_option("display.max_rows", 99999)


class PlotData:

    def __init__(self, anal, experiments, runs):
        self.anal = anal
        self.experiments = experiments
        self.runs = runs

        self.dir = 'experiments/anal/'
        self.measures = ['steps', 'total_success', 'total_hurt', 'rewards']
        self.measures_limits = [[20, 170],  [-0.5, 9.5], [-10, 1400], [-10, 100]]
        self.metrics = ['max', 'mean', 'min', 'median']
        self.clrs = ['#FF3333', '#006600']

        plt.style.use('classic')

    def lines(self):

        full_data_agreg = pd.read_csv(f'{self.dir}{self.anal}_full_data_agreg.csv')
        full_data_agreg = full_data_agreg[full_data_agreg['experiment'].isin(self.experiments)]

        pprint.pprint(full_data_agreg)

        for idx_measure, measure in enumerate(self.measures):

            for metric in self.metrics:
                fig, ax = plt.subplots()

                for idx_experiment, experiment in enumerate(self.experiments):

                    data = full_data_agreg[full_data_agreg['experiment'] == experiment]

                    ax.plot(data['checkpoint'], data[f'{measure}_{metric}'], label=experiment, c=self.clrs[idx_experiment])

                    if metric == 'median':
                        ax.fill_between(data['checkpoint'],
                                         data[f'{measure}_q25'],
                                         data[f'{measure}_q75'],
                                        alpha=0.3, facecolor=self.clrs[idx_experiment])

                    if metric == 'mean':
                        ax.fill_between(data['checkpoint'],
                                        data[f'{measure}_{metric}'] - data[f'{measure}_std'],
                                        data[f'{measure}_{metric}'] + data[f'{measure}_std'],
                                        alpha=0.3, facecolor=self.clrs[idx_experiment])

                    ax.set_ylim((self.measures_limits[idx_measure][0], self.measures_limits[idx_measure][1]))
                    plt.xlabel('Test')
                    plt.ylabel(f'{measure}_{metric}')
                    plt.title(self.anal)
                    #
                    ax.legend()

                    if measure.find('total_success') != -1:
                        plt.plot([1, 35], [7, 7], 'k--', linewidth=1.5)

                font = {'font.size': 20}
                plt.rcParams.update(font)

                plt.grid()
                plt.savefig(f'{self.dir}{self.anal}_{measure}_{metric}.png', bbox_inches='tight')

    def boxes(self):

        plt.clf()

        tests_combinations = list(combinations(self.experiments, 2))

        full_data_agreg = pd.read_csv(f'{self.dir}{self.anal}_full_data.csv')
        full_data_agreg = full_data_agreg[full_data_agreg['experiment'].isin(self.experiments)]
        data_filtered = pd.DataFrame()

        for experiment in self.experiments:
            for run in self.runs:

                exp_run = full_data_agreg[(full_data_agreg['experiment'] == experiment) & (full_data_agreg['run'] == run)]
                exp_run = exp_run[(exp_run['total_success'] == exp_run["total_success"].max())]
                exp_run = exp_run[exp_run['total_hurt'] == exp_run["total_hurt"].min()]
                exp_run = exp_run[exp_run['steps'] == exp_run["steps"].min()]
                exp_run = exp_run[exp_run['checkpoint'] == exp_run["checkpoint"].max()]

                data_filtered = pd.concat([data_filtered, exp_run], axis=0)

        pprint.pprint(data_filtered)

        for idx_measure, measure in enumerate(self.measures):
            sb.set(rc={"axes.titlesize": 23, "axes.labelsize": 23, 'ytick.labelsize': 21, 'xtick.labelsize': 21})
            sb.set_style("whitegrid")

            plot = sb.boxplot(x='experiment', y=measure, data=data_filtered,
                              palette=self.clrs, width=0.4, showmeans=True, linewidth=2, fliersize=6,
                              meanprops={"marker": "o", "markerfacecolor": "yellow", "markersize": "12"})

            # remove bonferroni correction?
            if len(tests_combinations) > 0:
                add_stat_annotation(plot, data=data_filtered, x='experiment', y=measure,
                                    box_pairs=tests_combinations,
                                    test='Wilcoxon', text_format='star', loc='inside', verbose=4)

            if measure.find('total_success') != -1:
                plot.axhline(7, ls='--', color="black")

            plot.set_ylim((self.measures_limits[idx_measure][0], self.measures_limits[idx_measure][1]))
            plt.title(self.anal)
            plot.get_figure().savefig(f'{self.dir}{self.anal}_{measure}_box.png', bbox_inches='tight')
            plt.clf()

analysis = {
     'foraging-TD':  ["foraging-TD"]
}


runs = range(1, 20+1)
for anal in analysis:
    cd = PlotData(anal, analysis[anal], runs=runs )
    cd.lines()
    cd.boxes()








