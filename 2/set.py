# set1 = {12,23,11,'hello'}
# set2 = {23,54,37,'world'}
# set3 = {12,37,24,'Mery'}
# for x in set1:
# 	print(x)
# print('11' in set1)

#Add
# set1.add(123)
# print(set1)

#Clear
# set2.clear()
# print(set2)

# COPY
# new_set = set1.copy()
# print(new_set)

# DElete
# set1.discard(12)
# print(set1)

#intersection krknvoxnerna berum

#difference hanuma tarberutyuny
# print(set1.difference(set2))

#set1.discard('helo') - ete ka jnjuma ete chka chi jnjum, remove - jnjum e ev erora berum ete chka

# x = {'apple','banana','cherry'}
# y = {'google','microsoft','apple'}
# z = x.symmetric_difference(y)
# print(z)

# miacnuma irar 
# set1.update(set2)
# print(set1)

# my_list = [12,32,45,21,32,12]
# num = []

# c = set(my_list)
# print(list(c))

# for i in my_list:
# 	if i not in num:
# 		num.append(i)
# print(num)

# c = set('hello')
# print(c)

# word = input('enter ')
# char = word[0]
# word = word.replace(char,'$')

# word = char + word[1:]
# print(word)

# str1 = 'abc'
# str2 = 'xyz'
# new_str = str1[:2] + str2[-1] + ' ' + str2[:2] + str1[-1] 
# print(new_str)

word = input('enter word ')
if len(word) > 2:
	if word[-3:] == 'ing':
		word += 'ly'
		print(word)
	else:
		word += 'ing'
		print(word)