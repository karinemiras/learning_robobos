import os
os.environ["KMP_WARNINGS"] = "FALSE"
import pandas as pd
from config import Config
import pprint
import sys
from experiment_manager import ExperimentManager

from foraging_seen import ForagingEnv as ForagingEnv
from foraging_mseen import ForagingEnv as ForagingmEnv
from avoiding_seen import ForagingEnv as AvoidingEnv
from avoiding_mseen import ForagingEnv as AvoidingmEnv

from stable_baselines3 import TD3
from stable_baselines3 import SAC



def load_td(name, env):
    return TD3.load(name, env)


def load_sac(name, env):
    return SAC.load(name, env)


def run_test(log_food_print, experiment, run, load, env, checkpoint):
    config.experiment_name = f'{experiment}_{run}'
    ExperimentManager(config=config,
                      model=None,
                      environment=env,
                      load=load,
                      log_food_print=log_food_print
                     ).test_policy(experiment, run, checkpoint)


def extract_info(experiment):

    algorithm = experiment.split("seen")[1]
    reward = experiment.split("seen")[0][-1]
    task = experiment.split("seen")[0][0]

    if algorithm == 'TD':
        load = load_td
    else:
        load = load_sac

    if task == 'f':
        if reward == 'm':
            env = ForagingmEnv(config=config)
        else:
            env = ForagingEnv(config=config)
    else:
        if reward == 'm':
            env = AvoidingmEnv(config=config)
        else:
            env = AvoidingEnv(config=config)

    return load, env


###
config = Config()
config = config.parser.parse_args()
config.robot_port = 19997
config.train_or_test = 'test'

# for final tests, run once with sim and once with hard
config.sim_hard = 'sim'
#config.sim_hard = 'hard'

log_food_print = True
experiments = ['avoidmseenSAC_7']

# very good!
# forseenTD_4

#choice or bests
tests_type = 'bests'


if tests_type == 'choice':

    experiment =  'avoidmseenSAC'
    run = '7'
    checkpoint = 35

    load, env = extract_info(experiment)
    run_test(log_food_print, experiment, run, load, env, checkpoint)


else:
    for exp in experiments:

        aux_str = exp.split('_')
        experiment = aux_str[0]
        run = aux_str[1]

        full_data_agreg = pd.read_csv(f'experiments/anal/{experiment}_full_data.csv')
        data_filtered = pd.DataFrame()

        exp_run = full_data_agreg[
            (full_data_agreg['experiment'] == experiment) & (full_data_agreg['run'] == int(run))]
        exp_run = exp_run[(exp_run['total_success'] == exp_run["total_success"].max())]
        exp_run = exp_run[exp_run['total_hurt'] == exp_run["total_hurt"].min()]
        exp_run = exp_run[exp_run['steps'] == exp_run["steps"].min()]
        exp_run = exp_run[exp_run['checkpoint'] == exp_run["checkpoint"].max()]

        data_filtered = pd.concat([data_filtered, exp_run], axis=0)

        pprint.pprint(data_filtered)

        for row in data_filtered.iterrows():

            checkpoint = row[1]["checkpoint"]
            run = row[1]["run"]

            load, env = extract_info(experiment)
            print('checkpoint', checkpoint)

            run_test(log_food_print, experiment, run, load, env, checkpoint)
