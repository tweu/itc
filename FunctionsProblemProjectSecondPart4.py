def menu():
	a = input('Что жрать будешь? ')
	b = input('Что пить будешь? ')
	c = open('/home/maxim/Рабочий стол/menu.txt', 'a')
	c.write(a)
	c.write(b)
	print(f'Ты будешь есть {a} и пить {b}')
	c.close()
menu()
