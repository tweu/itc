import os
def file():
	name = input("Введите название файла: ")
	os.system('touch /home/maxim/Рабочий\ стол/{}'.format(name))

a = file

a()
