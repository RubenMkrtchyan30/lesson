# color_phone = input('enter the color ') == 'red'
# phone_model = input('write model ') == 'iphone 7'
# res = color_phone and phone_model
# print('buy iphone', res)

# question1 = input('1 Meter = ? sm ') == '100'
# question2 = input('13 + 20 = ') == '33'
# question3 = input('2 * 12 = ') == '24'
# question4 = input('5^2 = ') == '25'
# question5 = input('sqrt(9) = ') == '3'
# result_question = question5 and question4 and question3 and question2 and question1
# print('patasxaneciq harcerin chisht',result_question)

# true_quest = '2 1'
# question6 = input('3 > ') 
# result = question6 in true_quest 
# print(question6)



# min_year = 17
# max_year = 25
# krtutyun_my = 'barcraguyn'
# python_my = 'python'

# year = int(input('qani tarekan eq ? '))
# python = input('inch cragravorman lezvi eq tirapetum ? ') == python_my
# krtutyun = input('inch krtutyun uneq duq ') == krtutyun_my

# user_year = min_year < year and max_year > year
# print('duq yndunvel eq',user_year and python and krtutyun)

# date = '2000 2001 2002 2003 2004 2005 2006'
# car = 'bmw mercedes audi kia mustang chevrolet hummer'
# color = 'red blue white black orange'

# user_date = input('vor tvakani meqena e dzez hetaqrqrum ? ')
# user_car = input('inch markayi meqena e petq? ')
# user_color = input('inch guyni meqena e petq? ')

# res = user_date in date and user_car in car and user_color in color

# print('menq unenq aydpisi meqena', res)

# a = 5
# b = 6
# res = ( a + b ) ** 3
# print(res)

import random

num = '1 5 7 8 9'

x = random.randint(1,10)
print('x =',x)

res = str(x) in num
print(res)