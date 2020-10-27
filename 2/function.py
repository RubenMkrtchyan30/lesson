# def test1():
# 	print('hello')
# test1()

# def test2(fname, lname):
# 	print(fname + ' ' + lname)
# test2('Emil', 'Sargsyan')

# def test2(fname, lname):
# 	print(fname + ' ' + lname)
# test2(lname = 'Emil', fname = 'Sargsyan')

# pass

# def country():
# 	pass

# def fruit_food(food):
# 	for x in food:
# 		print(x)
# fruit = ['apple','banan','cherry']
# fruit_food(fruit)

# def my_function(x):
# 	print(5 * x)
# c = my_function(3)
# print(c)

# def my_function():
# 	global x
# 	x = 5
# my_function()
# print(x)

# def myfunc(*x):
# 	print(x)

# myfunc(5,5,6,7,8)	


#dict in function

# def myfunc(**kwargs):
# 	print(kwargs)

# myfunc(name = 'Rub' , b = 4)	

#new funct

# add = lambda x,y: x+y
# print(add(2,5))

# calculate
def add(x,y):
	return x + y

def minus(x,y):
	return x-y

def multy(x,y):
	return x * y

def bajanum(x,y):
	return x / y

def yntr():
	global num1
	global choice
	global num2

	while True:
		num1 = input('enter num1 ')
		choice = input('+, -, *, / ')
		num2 = input('enter num2 ')	
		if num1.isdigit() and num2.isdigit():
			num1 = int(num1)
			num2 = int(num2)
			break
		else:
			print('please input number')	
 
def result():
	if choice == '+':
		print(add(num1,num2))
	if choice == '-':
		print(minus(num1,num2))
	if choice == '/':
		print(bajanum(num1,num2))
	if choice == '*':
		print(multy(num1,num2))
yntr()
result()