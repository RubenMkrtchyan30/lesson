# def maxoftwo(x,y):
# 	if x > y:
# 		return x
# 	return y

# x = int(input())
# y = int(input())
# print(maxoftwo(x,y))

# def sum(*args):
# 	c = 0
# 		for i in args:
# 			c+=i

# print(sum(x,y))

# def kmtomile(x):
# 	return x * 1.6
# print(kmtomile(5))

# def daytosec(x):
# 	return x * 24 * 60 *60
# print(daytosec(1))

# def validpassword(password):

# 	number = 0
# 	upper = 0
# 	for i in password:
# 		if i.isdigit():
# 			number += 1
# 		elif i.isupper():
# 			upper +=1
# 	if number > 1 and upper > 0 and len(password) > 7:
# 		return 'true'
# 	else:
# 		return 'false'

# pas = input('enter pass ') 
# print(validpassword(pas))

def fact(num):
	
	res = 1

	for i in range(1,num+1):
		res = res * i
	return res
	
number = int(input('enter'))
print(fact(number))