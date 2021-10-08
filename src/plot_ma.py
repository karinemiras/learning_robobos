import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pprint

pd.set_option("display.max_rows", 99999)


class PlotData:

    def __init__(self, anal, experiments, runs):
        self.anal = anal
        self.experiments = experiments
        self.runs = runs
        self.full_data_agreg = None

        self.dir = 'experiments/anal/'
        self.measures = ['steps_ma', 'total_success_ma', 'total_hurt_ma', 'rewards_ma']
        self.measures_limits = [[130, 220],  [-0.5, 9.5], [-10, 1400], [0, 800]]
        self.clrs = ['#CC0000', '#006600']
        plt.style.use('classic')

    def read(self):
        self.full_data_agreg = pd.read_csv(f'{self.dir}{self.anal}_full_data_ma.csv')
        self.full_data_agreg = self.full_data_agreg[self.full_data_agreg['experiment'].isin(self.experiments)]

    def lines(self):

        for idx_measure, measure in enumerate(self.measures):

            fig, ax = plt.subplots()
            for run in self.runs:

                data = self.full_data_agreg[self.full_data_agreg['run'] == run]
                color = np.random.uniform(0, 1, 3)

                ax.plot(data['episode'], data[f'{measure}'], c=color, alpha=0.5, linewidth=2, label=run)

                ax.set_ylim((self.measures_limits[idx_measure][0], self.measures_limits[idx_measure][1]))
                plt.xlabel('Episode')
                plt.ylabel(f'{measure}')
                plt.title(self.anal)
                #ax.legend()

                if measure.find('total_success') != -1:
                    plt.plot([1, 400], [7, 7], 'k--', linewidth=1)

            font = {'font.size': 20}
            plt.rcParams.update(font)

            plt.grid()
            plt.savefig(f'{self.dir}{self.anal}_{measure}.png', bbox_inches='tight')

    def scatter(self):
        columns = 5
        rows = 2
        run = 0

        plt.rc('xtick', labelsize=17)
        plt.rc('ytick', labelsize=17)
        fig, axs = plt.subplots(rows, columns, sharex=True, sharey=True, constrained_layout=True)

        for row in range(0, rows):
            for column in range(0, columns):
                run = run + 1
                data = self.full_data_agreg[self.full_data_agreg['run'] == run]
                pprint.pprint(data)
                axs[row, column].scatter(data['total_success_ma'], data['total_hurt_ma'], c=data['episode'],
                                         cmap='jet', alpha=0.5, linewidth=0)

                plt.xticks([0, 7])
                plt.yticks([0])

        plt.savefig(f'{self.dir}{self.anal}_ratio.png')


analysis = {
     'foraging-TD':  ["foraging-TD"]
}


runs = range(1, 21+1)

for anal in analysis:
    cd = PlotData(anal, analysis[anal], runs)
    cd.read()
    cd.lines()
    cd.scatter()








