s = 'Integers 1,2,3 Floats 44 Strings 5 Lists 10Tuples' 
numbers = []
letters =[]
for i in s:
	if i.isdigit():
		numbers.append(i)
	elif i.isalpha():
		letters.append(i)
print(numbers)
print(letters)
