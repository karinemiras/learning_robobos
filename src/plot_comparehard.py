import pprint
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from statannot import add_stat_annotation
from itertools import combinations
import sys

pd.set_option("display.max_rows", 99999)


dir = 'experiments/anal/'

data_sim = pd.read_csv(f'{dir}final_tests_sim.txt', sep="\t", header=None)
data_sim.columns=["experimentrun", "type", "pos", "total_success", "total_hurt", "steps"]


data_hard = pd.read_csv(f'{dir}final_tests_hard.txt', sep=" ", header=None)
data_hard.columns=["pos", "total_success"]
data_hard["type"] = 'hard'

data_sim = data_sim[data_sim['experimentrun'] == 'h_foraging-TD_12']

data_sim = data_sim.drop(columns=["experimentrun","pos", "total_hurt", "steps"])
data_hard = data_hard.drop(columns=[ "pos"])

data = pd.concat([data_sim, data_hard])

pprint.pprint(data)

clrs = ['#000066', '#006600']


sb.set(rc={"axes.titlesize": 23, "axes.labelsize": 23, 'ytick.labelsize': 21, 'xtick.labelsize': 21})
sb.set_style("whitegrid")

plot = sb.boxplot(x='type', y="total_success", data=data,
                  palette=clrs, width=0.4, showmeans=True, linewidth=2, fliersize=6,
                  meanprops={"marker": "o", "markerfacecolor": "yellow", "markersize": "12"})


add_stat_annotation(plot, data=data, x='type', y="total_success",
                    box_pairs=[('sim', 'hard')],
                    comparisons_correction=None,
                    test='Wilcoxon', text_format='star', fontsize='xx-large', loc='inside', verbose=1, line_height=0.4)


plot.axhline(7, ls='--', color="blue", alpha=0.7)
plot.set_ylim(-0.5, 8.5)
plot.set(xlabel='environment', ylabel='total_success')

#plt.title(self.anal)
plot.get_figure().savefig(f'{dir}hardware_box.png', bbox_inches='tight')
plt.clf()










