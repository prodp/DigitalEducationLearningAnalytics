# Squat QUIZ
squat_quiz_usecols = [1, 2, 3, 4, 5]
squat_quiz_cols = ['id', '0', '1', '2', '3']

squat_quiz_question_dict = {
    0:'Which of the following muscles are NOT primary muscles for the squat?',
    1:'This person is doing something wrong during the squat, which mistakes can you identify in the image?',
    2:'Which of the following images show the good position of you lower body during the squat?',
    3:'What could happen if you don\'t do the squat correctly ?'
}

squat_quiz_solutions = {
    0:[['a)', 'b)', 'd)'], ['a)', 'b)', 'c)', 'd)', 'e)']],
    1:[['b)', 'c)'], ['a)', 'b)', 'c)']],
    2:[['a)'], ['a)']],
    3:[['c)'], ['a)', 'b)', 'c)']]
}

# Pushup QUIZ
pushup_quiz_usecols = [1, 2, 3, 4, 5]
pushup_quiz_cols = ['id', '0', '1', '2', '3']

pushup_quiz_question_dict = {
    0:'Which of the following muscles are NOT primary muscles for the pushup?',
    1:'This person is doing something wrong during the pushup, which mistakes can you identify in the image?',
    2:'Which of the following actions can help you keep the back straight?',
    3:'Which of the following images show a possible pushup variant?'
}

pushup_quiz_solutions = {
	0:[['b)', 'e)'], ['a)', 'b)', 'c)', 'd)', 'e)']],
	1:[['b)'], ['b)']],
	2:[['c)'], ['c)']],
	3:[['a)'], ['a)']]
}

# Final quiz
final_quiz_usecols = [1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16]
final_quiz_cols = ['id', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

final_quiz_question_dict = {
	0:"In your opinion, is this similar to one of the exercises shown during the lecture? If yes, which one?",
	1:"Select all correct statements regarding pushups",
	2:"What is the correct sequence of the Burpee we explained in this class?",
	3:"This muscle is trained by a squat",
	4:"This muscle is trained by a squat",
	5:"This injury can be the consequence of incorrect elbow movement during pushups",
	6:"In your opinion, is this similar to one of the exercises shown during the lecture? If yes, which one?",
	7:"Now, select all correct statements regarding squats",
	8:"The chaining of the Burpee explain could particularly hurt one body joint if done uncorrectly. Which joins are at risk?",
	9:"This muscle is trained by a pushup",
	10:"This injury can be the consequence of incorrect elbow movement during pushups",
	11:"It's a good idea to show this gif while teaching pushups."
}

q1_all = ['A planck is a variant of the pushup',
'Wide arms pushups train the same muscles as narrow arms ones',
'The abdominals act as stabilizer muscles',
'Arms should never be fully extended in order to avoid elbow injuries',
'There are easier pushup variants for beginners',
'A pushup mainly involves three primary muscles',
'Pelivs should be rotated towards the head',
'Quantity > Quality',
'Keeping the back straight makes the exercise easier',
'You should pay attention to what your elbows are doing',]

q1_correct = ['The abdominals act as stabilizer muscles',
'There are easier pushup variants for beginners',
'A pushup mainly involves three primary muscles',
'You should pay attention to what your elbows are doing',]

q7_all = [
'A lunge is a variant of the squat.',
'Feet should always be wider than shoulder width and point outward.',
'The muscles of the back aren\'t important for the squat.',
'Flexibility isn\'t important for the squat.',
'Arms crossed forward help keep balance.',
'Knees should extend beyond the toes.',
'Body weight should remain on the toes.',
]

q7_correct = [
'Feet should always be wider than shoulder width and point outward.',
'Arms crossed forward help keep balance.',
]

q8_all = [	
'Knee joints',
'Wrist joints',
'Ankle Joint',
'Elbow joint',
'Hip Joint',
'Shoulder'
]

q8_correct = [	
'Knee joints',
'Hip Joint',
]

final_quiz_solutions = {
	0:['manual'],
	1:[q1_correct, q1_all],
	2:[['Squat -> Jump -> Pushup'], ['Squat -> Jump -> Pushup']],
	3:['scale', 5],
	4:['scale', 1],
	5:['scale', 1],
	6:['manual'],
	7:[q7_correct, q7_all],
	8:[q8_correct, q8_all],
	9:['scale', 2],
	10:['scale', 5],
	11:['scale', 5]
}

# Summary
cleanup_dicts = {
	'squat':[squat_quiz_usecols, squat_quiz_cols, squat_quiz_question_dict, squat_quiz_solutions],
	'pushup':[pushup_quiz_usecols, pushup_quiz_cols, pushup_quiz_question_dict, pushup_quiz_solutions],
	'final':[final_quiz_usecols, final_quiz_cols, final_quiz_question_dict, final_quiz_solutions]
}