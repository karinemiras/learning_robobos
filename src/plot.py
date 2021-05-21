import glob
import numpy as np
import pickle
import pprint
import pandas as pd
import matplotlib.pyplot as plt
import sys

pd.set_option("display.max_rows", 99999)


class PlotData:

    def __init__(self):

        self.dir = 'experiments/'

    def run(self):

        measures = ['steps', 'duration', 'total_success', 'rewards', 'step_success']
        metrics = ['max', 'mean', 'min', 'median']
       #  measures = ['total_success']
       #  metrics = ['mean']



        full_data_agreg = pd.read_csv(f'{self.dir}consolidated.csv')

        print(full_data_agreg)

        for measure in measures:
            for metric in metrics:

                fig, ax = plt.subplots()

                for key, grp in full_data_agreg.groupby(['experiment']):
                    ax = grp.plot(ax=ax, kind='line', x='episode', y=f'{measure}_{metric}' , label=key) #c=color
                    # ax = ax.fill_between(total_success_mean, total_success_mean - total_success_std, total_success_mean + total_success_std,
                    #                  color='gray', alpha=0.2)

                plt.legend(loc='best')
                plt.savefig(f'{self.dir}{measure}_{metric}.png')

cd = PlotData()

cd.run()








