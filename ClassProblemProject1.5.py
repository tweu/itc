class School:

	def __init__(self, teacher, students):
		self.teacher = teacher
		self.students = students

	def __str__(self):
		return f'{self.teacher} {self.students}'


my_class = School(teacher = 'Inna Yurievna', students = ['me', 'my ofnoklassniki'])
print(my_class)
