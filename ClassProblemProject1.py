class Group:

	def __init__(self, name, students):
		self.name = name
		self.students = students
		self.amount = self.amountofstudents()

	def __str__(self):
		return f'{self.name} {self.amount}'


	def amountofstudents(self):
		amount = len(self.students)
		return amount

group = Group('Python3', ['Bermet, Aelita, Yrys', 'ya'])
print(group.students)
print(group.amount)
print(group.amountofstudents)
	
group2 = Group('Вторая групппа', ['Hello'])
print(group2.students)