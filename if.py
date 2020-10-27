#factorial

# import math
# print(math.factorial(5))

# a = 27
# b = 14
# if a > b:
# 	print('a is big')

# a = 34
# b = 14

# if b > a:
# 	print('b is big')
# elif a > b:
# 	print('a is big')

# a = 34
# b = 14
# if b > a:
# 	print('b is big')
# z = 7
# c = 7
# if z == c:
# 	print('ok') 

# c = 12
# d = 27
# result = a > b and d > c
# if result:
# 	print('a and d are biger')

# human and dogs year old

# human_year = int(input('enter human year '))
# if human_year == 0:
# 	print('Dog year = 0')
# elif human_year < 0:
# 	print('enter positiv integer')
# elif human_year <= 2 and human_year > 0:
# 	print('Dog year =',human_year * 5.25 )
# elif human_year >= 2:
# 	human_year1 = 10.5 + (human_year - 2) * 4
# 	print(human_year1)

import random as r
user_point = 0
pc_point = 0
random = r.randint(1, 3)
user = int(input('enter your number(1-3) '))
print('pc =',random,'\nuser =',user,)

if user == random:
	user_point += 1
	print('user point = ',user_point)
else:
	pc_point += 1
	print('user point = 0')

random = r.randint(1, 3)
user = int(input('enter your number(1-3) '))
print('pc =',random,'\nuser =',user,)

if user == random:
	user_point += 1
else:
	pc_point += 1
if user_point == 2:
	print('you win user point = ',user_point)
elif pc_point == 2:
	print('you lose')
else:
	print('1:1')