class Student:
	
	def __init__(self, name):
		self.name = name
	
	
	def say_hello(self):
		print('Hello, my name is', self.name)
	
obj = Student('John')
obj.say_hello()
