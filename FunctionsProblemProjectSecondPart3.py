def dictionary(dictionary1, dictionary2):
	dictionary1.update(dictionary2)
	return dictionary1
dictionary1 = {'name': 'Yrys'}
dictionary2 = {'age': '20'}
print(dictionary1)
print(dictionary2)
a = dictionary(dictionary1, dictionary2)
print(a)