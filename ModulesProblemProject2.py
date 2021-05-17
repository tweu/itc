import random
list = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai","Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan","Maksat"]
list2 = []
for _ in range(1, 5):
	a = random.choice(list)
	print(a)
	list2.append(a)
	print(list2)