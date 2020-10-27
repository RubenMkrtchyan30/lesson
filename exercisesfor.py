# for i in range(1,12*15+1):
# 	if i % 12 == 0 and i % 15 == 0:
# 		print(i)
# 		break
# i = 1
# while True:
# 	if i % 12 == 0 and i % 15 == 0:
# 		print(i)
# 		break
# 	i +=1	

# odd = 0
# even = 0

# for i in range(1,101):
# 	if i % 2 == 0:
# 		even += 1
# 	else:
# 		odd += 1

# print('odd =',odd,'even =',even)

#fibonacci
# x,y = 0,1

# while y < 40:
# 	print(y)
# 	x,y = y,x+y
	
# letters = 0
# numbers = 0	
# string = 'python 3.9'
# for i in string:
# 	if i .isalpha():
# 		letters += 1
# 	elif i.isdigit():
# 		numbers += 1
# print(letters)
# print(numbers)

# num =73421
# res = 0

# for i in str(num):
# 	res += int(i)
# print(res)

# factorial
# x = int(input('enter number '))
# res = 1
# for i in range(1,x+1):
# 	res *= i
# print(res) 


# while True:
# 	age = int(input('your age = '))
# 	if   17 < age < 21:
# 		print('yndunvac eq	')
# 		break
# 	print('no')	

#21 
import random

start = input('xax@ duq skseq? ')
yes = start == 'y'
if yes:
	user = input('dzer tiv@ ')
else:
	random.randint(1,3)