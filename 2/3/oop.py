# class MyClass:
# 	x = 5

# print(MyClass)

# p1 = MyClass()
# print(p1.x)

# class Person:
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age


# 	def myfunc(self):
# 		print('hello my name is '+ self.name, self.age)

# p1 = Person("John",36)
# p1.myfunc()


# print(p1.name)
# print(p1.age)

# p2 = Person("Dav",20)

# print(p2.name)
# print(p2.age)

class Calculator:
	'''Create Calculate'''

	def __init__(self,x,choice,y):
		self.x = x
		self.choice = choice
		self.y = y

	def add(self):
		return self.x + self.y
	
	def minus(self):
		return self.x - self.y

	def multy(self):
		return self.x * self.y

	def division(self):
		return self.x / self.y



x = float(input('num1: '))
choice = input('+ - / * ')
if choice =='/':
	while  True:		
		y = float(input('num2: '))
		if y != 0:
			break
else:
	y = float(input('num2: '))
res = Calculator(x,choice,y)

if choice == '+':
	print(res.add())


if choice == '-':
	print(res.minus())

elif choice == '*':
	print(res.multy())

elif choice == '/':
	print(res.division())