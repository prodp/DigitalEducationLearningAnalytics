import pandas as pd
import numpy as np
import json

from utils_quizzes import *
from utils_sessions import *

# Globals
NUM_SESSIONS = 6
DATA = 'data/'
CLEAN = 'clean/'


# Cleanup functions
def cleanup_groups(session):
	if not in_groups[session]:
		df = pd.DataFrame(data={'id':list(participants[session].values()), 'partner':'null'})
	else:
		participants_path = DATA + str(session) + '/participants.json'
		with open(participants_path) as f:
			students_dict = json.load(f)['globalStructure']['students']
            
		groups_path = DATA + str(session) + '/groups.json'
		with open(groups_path) as f:
			groups = list(json.load(f)['socialStructure']['group'].values())
            
		parts = []
		partner = []
		for p in students_dict.keys():
			parts.append(participants[session][students_dict[p]])
			if p in groups[0]:
				if p == groups[0][0]:
					partner.append(participants[session][students_dict[groups[0][1]]])
				else:
					partner.append(participants[session][students_dict[groups[0][0]]])
			elif p in groups[1]:
				if p == groups[1][0]:
					partner.append(participants[session][students_dict[groups[1][1]]])
				else:
					partner.append(participants[session][students_dict[groups[1][0]]])
		df = pd.DataFrame(data={'id':parts, 'partner':partner})
        
	filename = DATA + CLEAN + 's' + str(session) + '_groups.csv'
	df.to_csv(filename, encoding='utf-8')
	return df


def map_to_points_pretest(q, a):
    if q == 0:
        return (4-a)*0.25
    elif q == 1:
        return 1-a
    else:
        correct = [1, 3, 5]
        points = 0;
        for o in range(6):
            if str(o) in a.keys() and o in correct:
                points += 1
            elif str(o) not in a.keys() and o not in correct:
                points += 1
        return points/6


def cleanup_pretest(session):
	participants_path = DATA + str(session) + '/participants.json' ;
	with open(participants_path) as f:
		students_dict = json.load(f)['globalStructure']['students']

	pretest_path = DATA + str(session) + '/pretest.json' ;
	with open(pretest_path) as f:
		payload = json.load(f)['payload']
		p = []
		q1 = []
		q2 = []
		q3 = []
		for participant in payload:
			a_mask = payload[participant]['data']['answersIndex']
			q3_mask = payload[participant]['data']['form']['2']
			p.append(participants[session][students_dict[participant]])
			q1.append(map_to_points_pretest(0, a_mask[0]))
			q2.append(map_to_points_pretest(1, a_mask[1]))
			q3.append(map_to_points_pretest(2, q3_mask))
		
        # Write dataframe to cleaned folder
		df = pd.DataFrame(data={'id':p, '0':q1, '1':q2, '2':q3})
		total = df[['0', '1', '2']].sum(axis=1)
		df['total'] = total
		df['percent'] = (total/3)*100
		
		filename = DATA + CLEAN + 's' + str(session) + '_pretest.csv'
		df.to_csv(filename, encoding='utf-8')
		
		return df


def map_to_points(question, answer, answer_dict):
    if answer_dict[question][0] == 'manual':
        return answer
    elif answer_dict[question][0] == 'scale':
        return (4 - abs(answer_dict[question][1] - int(answer)))/4
    else:
        points = 0;
        for p in answer_dict[question][1]:
            if (p in answer and p in answer_dict[question][0]) or (p not in answer and p not in answer_dict[question][0]):
                points += 1
        return points/len(answer_dict[question][1])

	
def cleanup_quiz(quiz, session):
	'''
	Cleans up either a squat or pushup quiz, mapping names to ids and answers to scores
	'''
    # Read csv
	raw_filename = DATA + str(session) + '/' + quiz + '.csv'
	df_quiz = pd.read_csv(raw_filename, encoding='utf-8', quotechar='"', sep=',', header=0,
					usecols=cleanup_dicts[quiz][0], names=cleanup_dicts[quiz][1])

	# Map participants to ids
	df_quiz.id = df_quiz.id.apply(lambda name: participants[session][name])

	# Map answers to points
	for q in range(len(cleanup_dicts[quiz][2])):
		df_quiz[str(q)] = df_quiz[str(q)].apply(lambda a: map_to_points(q, a, cleanup_dicts[quiz][3]))

	# Write dataframe to cleaned folder
	sum_col = ['0', '1', '2', '3'] if (quiz == 'squat' or quiz == 'pushup') else ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
	total = df_quiz[sum_col].sum(axis=1)
	df_quiz['total'] = total
	df_quiz['percent'] = (total/len(sum_col))*100
	filename = DATA + CLEAN + 's' + str(session) + '_' + quiz + '.csv'
	df_quiz.to_csv(filename, encoding='utf-8')

	return df_quiz


# Cleanup each session
for s in range(NUM_SESSIONS):
	# Handle groups
	cleanup_groups(s)
	
	# Handle pre-quiz
	cleanup_pretest(s)

	# Handle intermediate quizzes
	cleanup_quiz('squat', s)
	cleanup_quiz('pushup', s)
	
	# Handle final quiz 
	cleanup_quiz('final', s)
	
	# Handle peer review TODO
	None