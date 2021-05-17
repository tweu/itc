import os
import random
os.system('mkdir /home/maxim/Рабочий\ стол/testdirectory'
for _ in range(1,6):
	a = random.randint(1, 100)
	os.system(f'touch /home/maxim/Рабочий\ стол/testdirectory/test{a}.txt')