# def my_function():
# 	print('Hello')

# my_function()

my_list=['hello', 'yeah']
def length():
	result = 0
	for _ in my_list:
		result+=1
	print('список состоит из {} элементов'.format(result))


def my_function():
	print("Ты не должен здесь быть")
	length()
length()
my_function()