import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option("display.max_rows", 99999)


class PlotData:

    def __init__(self, anal, experiments):
        self.anal = anal
        self.experiments = experiments
        self.runs = range(1, 10+1)

        self.dir = 'experiments/'
        self.measures = ['steps_ma', 'total_success_ma', 'rewards_ma']
        self.measures_limits = [[20, 150], [0, 9.5], [-10, 100]]
        self.clrs = ['#CC0000', '#006600']
        plt.style.use('classic')

    def lines(self):

        full_data_agreg = pd.read_csv(f'{self.dir}{self.anal}_full_data.csv')
        full_data_agreg = full_data_agreg[full_data_agreg['experiment'].isin(self.experiments)]

        print(full_data_agreg)

        for idx_measure, measure in enumerate(self.measures):

            fig, ax = plt.subplots()

            for run in self.runs:

                data = full_data_agreg[full_data_agreg['run'] == run]
                color = np.random.uniform(0, 1, 3)

                ax.plot(data['episode'], data[f'{measure}'], c=color, alpha=0.7, linewidth=2)

                ax.set_ylim((self.measures_limits[idx_measure][0], self.measures_limits[idx_measure][1]))
                plt.xlabel('Stage')
                plt.ylabel(f'{measure}')
                plt.title(self.anal)

                if measure.find('total_success') != -1:
                    plt.plot([1, 400], [7, 7], 'k--', linewidth=0.5)

            plt.grid()
            plt.savefig(f'{self.dir}{self.anal}_{measure}.png')


analysis = {
     #'forseenSAC':  ["forseenSAC"],
     'formseenSAC':  ["formseenSAC"]
}


for anal in analysis:
    cd = PlotData(anal, analysis[anal])
    cd.lines()
    #cd.boxes()








