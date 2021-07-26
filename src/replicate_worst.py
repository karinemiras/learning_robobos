import numpy as np
import pprint
import pandas as pd
import shutil, os

pd.set_option("display.max_rows", 99999)

class PlotData:

    def __init__(self, experiment):
        self.experiment = experiment
        self.dir = 'experiments/'

    def replicate(self, file):



        full_data_agreg = pd.read_csv(f'{self.dir}{self.experiment}_full_data.csv')
        full_data_agreg = full_data_agreg[full_data_agreg['episode'] == full_data_agreg["episode"].max()]
        full_data_agreg = full_data_agreg.sort_values(by=['total_success'])

        # fetches worst runs up to first quartile
        prop_worst = 0.25
        data_worst = full_data_agreg[0:int(full_data_agreg.shape[0]*prop_worst)]
        pprint.pprint(data_worst)
        file.write(f'\n{data_worst.to_string()}\n')

        for index, row in data_worst.iterrows():

            experiment_name_new = f"{experiment}_h_{row['run']}"

            # copying
            shutil.copytree(f'{self.dir}{experiment}_{row["run"]}', f'{self.dir}{experiment_name_new}')

            command = f'python3 src/{experiment}.py --experiment-name {experiment_name_new} ' \
                f'--training-timesteps 35000 --checkpoint-timesteps 1000\n'
            file.write(command)

experiments = [ 'for_seen_TD',
                'for_mseen_TD']

file = open(f'{self.dir}run_human_experiments.txt', "w")

for experiment in experiments:
    cd = PlotData(experiment)
    cd.replicate(file)

file.close()








