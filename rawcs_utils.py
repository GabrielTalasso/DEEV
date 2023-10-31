from Client.client import FedClient
from Server.server import FedServer
import pickle
import flwr as fl
import os
import numpy as np

from Client.data_loader import get_dataset

def get_rawcs_params(dataset = 'MotionSense'):

    if dataset == 'MotionSense':
        STRATEGY='rawcs-sp'
        NUM_CLIENTS=24
        NUM_CLASSES=6
        FIT_FRACTION=0.125
        EVAL_FRACTION=1.0
        MIN_FIT=2
        MIN_EVAL=2
        MIN_AVAIL=2
        LEARNING_RATE=0.001
        RESULTS_DIR='logs/MotionSense/'
        SIM_ID='MotionSense'
        DATASET_NAME='MotionSense'
        TRANS_THRESH=0.2
        DEVICES_PROFILES=f'Server/devices_profiles/profiles_sim_{DATASET_NAME}_seed_1.json'
        NETWORK_PROFILES=f'Server/devices_profiles/sim_1_num_clients_{NUM_CLIENTS}_num_rounds_250.pkl'
        SIM_IDX=1
        DATASET_PATH='/home/gabrieltalasso/DEEV/Client/data/motion_sense'
        NUM_ROUNDS=50
        D_TEMP_SET_SIZE=48
        EXPLORATION_FACTOR=0.9
        STEP_WINDOW=20
        PACER_STEP=2
        PENALTY=2.0
        CUT_OFF=0.95
        BLACKLIST_NUM=1000
        UTILITY_FACTOR=0.25
        BATTERY_WEIGHT=0.33
        CPU_COST_WEIGHT=0.33
        LINK_PROB_WEIGHT=0.33
        TARGET_ACCURACY=1.0
        LINK_QUALITY_LOWER_LIM=0.2
    
    if dataset == 'ExtraSensory':
        STRATEGY='rawcs-sp'
        NUM_CLIENTS=60
        NUM_CLASSES=7
        FIT_FRACTION=0.125
        EVAL_FRACTION=1.0
        MIN_FIT=2
        MIN_EVAL=2
        MIN_AVAIL=2
        LEARNING_RATE=0.001
        RESULTS_DIR='logs/ExtraSensory/'
        SIM_ID='ExtraSensory'
        DATASET_NAME='ExtraSensory'
        TRANS_THRESH=0.2
        DEVICES_PROFILES=f'Server/devices_profiles/profiles_sim_{DATASET_NAME}_seed_1.json'
        NETWORK_PROFILES=f'Server/devices_profiles/sim_1_num_clients_{NUM_CLIENTS}_num_rounds_250.pkl'
        SIM_IDX=1
        DATASET_PATH='/home/gabrieltalasso/DEEV/Client/data/ExtraSensory'
        NUM_ROUNDS=50
        D_TEMP_SET_SIZE=48
        EXPLORATION_FACTOR=0.9
        STEP_WINDOW=20
        PACER_STEP=2
        PENALTY=2.0
        CUT_OFF=0.95
        BLACKLIST_NUM=1000
        UTILITY_FACTOR=0.25
        BATTERY_WEIGHT=0.33
        CPU_COST_WEIGHT=0.33
        LINK_PROB_WEIGHT=0.33
        TARGET_ACCURACY=1.0
        LINK_QUALITY_LOWER_LIM=0.2


    input_shape = None
    samples_per_client = []
    for cid in range(NUM_CLIENTS):
        x_train, y_train, x_test, y_test = get_dataset(DATASET_NAME, DATASET_PATH, cid)
        input_shape = x_train.shape
        samples_per_client.append(len(x_train))

    rawcs_params = {'num_clients' : NUM_CLIENTS,
    'num_classes' : NUM_CLASSES,
    'fit_fraction' : FIT_FRACTION,
    'eval_fraction' : EVAL_FRACTION,
    'min_fit' : MIN_FIT,
    'min_eval' : MIN_EVAL,
    'min_avail' : MIN_AVAIL,
    'learning_rate' : LEARNING_RATE,
    'results_dir' : RESULTS_DIR,
    'sim_id' : SIM_ID,
    'transmission_threshold' : TRANS_THRESH,
    'devices_profile' : DEVICES_PROFILES,
    'network_profiles' : NETWORK_PROFILES,
    'sim_idx' : SIM_IDX,
    'input_shape' : input_shape,
    'battery_weight' : BATTERY_WEIGHT,
    'cpu_cost_weight' : CPU_COST_WEIGHT,
    'link_prob_weight' : LINK_PROB_WEIGHT,
    'target_accuracy' : TARGET_ACCURACY,
    'link_quality_lower_lim' : LINK_QUALITY_LOWER_LIM,
    'clients_info': {},
    'time_percentile' : 95,
    'comp_latency_lim' : np.inf,
    'clients_last_round' : [],
    'max_training_latency' : 0.0,
    'limit_relationship_max_latency' : 0}

    return rawcs_params

