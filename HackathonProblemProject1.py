# print('Добро пожаловать в простейший калькулятор на Python!')
# sybmbol = input('Выберите знак операции: +, -, *, /')
# if '+' in sybmbol:
# 	print("Вы выбрали +")
# 	plus = float(input('Введите первое значение: '))
# 	plus2 =	float(input('Введите Второе  значение: '))
# 	res = plus + plus2
# 	print("Ваш результат: ", res)
# elif '-' in sybmbol:
# 	print("Вы выбрали -")
# 	minus = float(input('Введите первое значение: '))
# 	minus2 =	float(input('Введите Второе  значение: '))
# 	res2 = minus - minus2
# 	print("Ваш результат: ", res2)
# elif '*' in sybmbol:
# 	print("Вы выбрали *")
# 	multiply = float(input('Введите первое значение: '))
# 	multiply2 =	float(input('Введите Второе  значение: '))
# 	res3 = multiply + multiply2
# 	print("Ваш результат: ", res3)
# elif '/' in sybmbol:
# 	print("Вы выбрали /")
# 	divide = float(input('Введите первое значение: '))
# 	divide2 =	float(input('Введите Второе  значение: '))
# 	if divide == 0 or divide2 == 0:
# 		print('На ноль делить нельзя!')
			
# 	else:
# 		res4 = divide // divide2
# 		print("Ваш результат: ", res4)

#сверху не идет повторно



print("цифра 0 завершит цикл")
while True:
    s = input("Знак (+,-,*,/): ")
    if s == '0':
    	break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак операции!")


#идет поторно