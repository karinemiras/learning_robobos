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

        self.dir = 'experiments/old2/'

    def run(self):

        measures = ['steps', 'duration', 'total_success', 'rewards', 'step_success']
        metrics = ['max', 'mean', 'min', 'median']

        full_data_agreg = pd.read_csv(f'{self.dir}consolidated.csv')

        for measure in measures:
            for metric in metrics:

                fig, ax = plt.subplots()

                for key, grp in full_data_agreg.groupby(['experiment']):
                    ax = grp.plot(ax=ax, kind='line', x='episode', y=f'{measure}_{metric}' , label=key) #c=color

                plt.legend(loc='best')
                plt.savefig(f'{self.dir}{measure}_{metric}.png')

cd = PlotData()

cd.run()








