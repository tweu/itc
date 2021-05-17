class Car:

	def __init__(self , marka, color, year, model):
		self.marka = marka
		self.color = color
		self.year = year
		self.model = model


	def __str__(self):
		return f'{self.marka} {self.model} '

	def drive(self):
		return('Я еду')

	def my_method(self):
		print(self.marka)
		self.drive()

car1 = Car(marka = 'Mers', color= 'black', year='10202', model='222')
car2 = Car('Toyota', 'Red', 2102, 'Camry')


print(car1.marka, car1.model)

print(car2)	
print(car2.drive())