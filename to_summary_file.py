import pandas as pd
import numpy as np
import json

from utils_quizzes import *
from utils_sessions import *

# Globals
NUM_SESSIONS = 6
DATA = 'data/'
CLEAN = 'clean/'
BASE_PATH = DATA + CLEAN

def session_summary(session):
    df_groups = pd.read_csv(BASE_PATH + 's' + str(session) + '_groups.csv')
    df_groups.index = df_groups.id
    df_groups = df_groups[['partner']]

    df_pretest = pd.read_csv(BASE_PATH + 's' + str(session) + '_pretest.csv')
    df_pretest.index = df_pretest.id
    df_pretest = df_pretest[['total', 'percent']]
    df_pretest.columns = ['pretest_total', 'pretest_percent']

    df_squat = pd.read_csv(BASE_PATH + 's' + str(session) + '_squat.csv')
    df_squat.index = df_squat.id
    df_squat = df_squat[['total', 'percent']]
    df_squat.columns = ['squat_total', 'squat_percent']

    df_pushup = pd.read_csv(BASE_PATH + 's' + str(session) + '_pushup.csv')
    df_pushup.index = df_pushup.id
    df_pushup = df_pushup[['total', 'percent']]
    df_pushup.columns = ['pushup_total', 'pushup_percent']

    df_final = pd.read_csv(BASE_PATH + 's' + str(session) + '_final.csv')
    df_final.index = df_final.id
    df_final = df_final[['total', 'percent']]
    df_final.columns = ['final_total', 'final_percent']

    return df_groups.join([df_pretest, df_squat, df_pushup, df_final])

df_summary = pd.DataFrame()
for s in range(NUM_SESSIONS):
	df_session = session_summary(s)
	df_summary = df_summary.append(df_session)
	
df_summary.to_csv(BASE_PATH + 'summary.csv', encoding='utf-8')