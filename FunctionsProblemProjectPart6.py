import random
list1 =['maxim', '13yo', 'student', 'ITCBootcampstudent']
def divide():
	length = len(list1)
	polovina = length//2
	ppolovina = list1[0 : polovina]
	vpolovina = list1[polovina : ]
	ppolovina = list(reversed(ppolovina))
	vpolovina = list(reversed(vpolovina))
	res = ppolovina+vpolovina
	print(res)
divide()