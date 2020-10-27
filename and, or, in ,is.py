#and

# x = 4 
# result = x < 5 and x < 10
# print(result)

#or

# res = x < 5 or x > 10
# print(res)

#not

# resnot = not(x < 5 or x < 10)
# print(resnot)

# x = 6
# y = 6 
# print( x is y)
# name = 'Aram'
# name2 = 'aram'
# print(name is name2)

# x = 6
# y = 6 
# print( x is not y)
# name = 'Aram'
# name2 = 'aram'
# print(name is not name2)

# about_me = 'I am Ruben Mkrtchyan i have Covid19. sorry my friends i can not ...'
# word = 'Covid19'
# name = 'Ruben'
# result = word and name in about_me
# print(result)

# result_not = word not in about_me
# print(result_not)

# comment = 'My name is Ruben mkrtchyan.I was born in 25.03.2000'
# word1 = 'Ruben'
# word2 = 'Covid19'
# word3 = '10.03.2000'
# result = word1 in comment or word2 in comment or word3 in comment
# print(result)

# hancagorcutyun = 'jam@ 7 in petqa gnanq goxutyun katarelu'
# word1 = 'goxutyun'
# word2 = 'katarelu'
# word3 = 'hancagorc'
# result =  word1 in hancagorcutyun and (word2 in hancagorcutyun or word3 in hancagorcutyun)
# print(result)

item_bread = input('have you bread in home? ')=='y'
item_chicken = input('have you a chicken? ')=='y'
item_light = input('have you light? ')=='y'
market_chicken = input('go to market and buy a chicken? ')=='y'
market_bread = input('go to market and buy a bread? ')=='y'
buy_chicken = market_chicken and not item_chicken
buy_bread = market_bread and not item_bread
hanel_bread = item_bread and not item_light 
hanel_chicken = item_chicken and not item_light
print('hanel banany ' + str(hanel_bread))
print('haneq hav@ sarnaranic ' + str(hanel_chicken))

print('gneq hav xanutic '  + str(buy_chicken))
print('gneq hac xanutic '  + str(buy_bread))