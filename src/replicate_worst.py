import numpy as np
import pprint
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from statannot import add_stat_annotation
from itertools import combinations

pd.set_option("display.max_rows", 99999)

class PlotData:

    def __init__(self, anal):
        self.anal = anal
        self.dir = 'experiments/'

    def replicate(self):


        full_data_agreg = pd.read_csv(f'{self.dir}{self.anal}_full_data.csv')

        full_data_agreg = full_data_agreg[full_data_agreg['episode'] == full_data_agreg["episode"].max()]
        pprint.pprint(full_data_agreg)
        full_data_agreg = full_data_agreg.sort_values(by=['total_success'])
        pprint.pprint(full_data_agreg)
        # fetches worst runs up to first quartile
        data_worst = full_data_agreg[0:int(full_data_agreg.shape[0]*0.25)]
        pprint.pprint(data_worst)


analysis = [ 'for_seen_TD',
             'for_mseen_TD']

for anal in analysis:
    cd = PlotData(anal)
    cd.replicate()








