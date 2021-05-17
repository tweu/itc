# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = 5
# for i in a:
# 	if i >= 5:
# 		print(i)

#2 task
# digits = (113, 118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# for i in digits:
# 	res = i / 9
# 	print(res)


#3 task
# fruits = ('banana','stawberry','apple','orange','limon','ananas')
# print(fruits[0])
# print(fruits[-1])

#4 task
# spisok_1 = ( 'Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
# a = set(spisok_1)
# b = set(spisok_2)
# c= a.difference(b)
# print(c)

#5 task
# a = input("Введите прдложение не менее 6 слов")
# split1 = a.split()
# if len(split1)>=6:
# 	o = split1[:len(split1)//2]
# 	l = split1[len(split1)//2:]
# 	list1 =[]
# 	list1.extend(l)
# 	list1.extend(o)
# 	print(list1)


#6 task
# numbers = [2,4,7,1,8.4,-3.3,7.1,-2,4,-1,7,-43,8,-3,6,9]
# a = 0
# b = 0
# for i in numbers:
# 	if i % 2 == 0 and i / 2:
# 		a +=1
# 		print("s",a)
# 	else:
# 		b += 1
# 		print("1",b)
# print(a)
# print(b)

#7 task
numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
b = []
for i in numbers:
	if b <= -1:
		b.append(-1)
	elif b >= 1:
		b.append(1)
	else:
		b == 0
		b.append(0)
print(b)