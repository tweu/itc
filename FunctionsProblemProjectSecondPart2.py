def function(slovo):
	count = 0
	for i in slovo:
		if i.isalpha():
			count = count + 1
	return count




vodka = input('введи что нить: ')
a = function(vodka)
print(a)
