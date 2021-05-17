import sys
import os
a = input('Введите первое значение: ')
b = input('Введите второе значение: ')
c = sys.getsizeof(a)
d = sys.getsizeof(b)
print(c, d)
if c < d:
	print('c < d')
else:
	print('d > c')

