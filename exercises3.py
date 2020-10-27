# nahanj
# nahanj = int(input('mutqagreq taretivy '))
# payman1 = nahanj % 4 == 0
# payman2 = nahanj % 100 == 0
# payman3 = nahanj % 400 != 0
# if payman3 or payman1 and payman2:
# 	print('nahanj tari e ')
# else:
# 	print('nahanj che ')

# import random

# x = 'abcash'

# r = random.choice(x)
# print(r)

# value = int(input('enter value '))
# value2 = int(input('enter value '))

# if value > value2:
# 	print(value)

# elif value == value2:
# 	print("equel")

# else:
# 	print(value2)
# 

# x = 1234
# first_number = x // 1000
# first_result = x % 1000
# second = first_result // 100
# second_result = first_result % 100
# third = second // 10
# fourth = second % 10

# # print(c1,fourth,second,first_number)

# result = ''
# result += str(fourth) + str(third) + str(second) + str(first_number)
# print(int(result))

age = int(input('enter age '))
sex = input('m / f ') 
marital_status = input('are you married? (y/n) ')

if sex == 'f' and marital_status == 'y':
	print('you lose')
elif sex == 'f' or sex == 'm' and 60 > age > 40:
	print('you can work only urban areas')
elif sex == 'm' and 20 < age < 40:
	print('you can work in anywhere ')
else:
	print('ERROR')