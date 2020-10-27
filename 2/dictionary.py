# thisdict ={'name':'Aram','year':1994,'surname':'Sargsyan','day':20,'month':'March'}
# print(thisdict)

# pop = thisdict.popitem()
# print(pop) #vercnum e verjiny


# thisdict['year'] = 2014
# thisdict['b'] = 300
# print(thisdict)

# for i in range(10):
# 	thisdict[i] = 5
# print(thisdict)

# new_dict = {}

# for i,j in thisdict.items():
# 	new_dict[i] = j
# print(new_dict) #texapoxuma thisdicti parunakutyuny new_dict i mej

# print(i,j) # printa anum keyn u valuen

#  my_list = []
# a = {'a':1, 'b':2,'c':5,'d':0}

# for i in a.values():
# 	my_list.append(i)

# my_list.sort()
# print('min = ',my_list[0])
# print('max =',my_list[-1])

# print(sum(my_list)/len(my_list)) # mijin tvabanakan

# a['key'] = 12
# print(a)

num_list = [387,544,5,6,7,6,2,4]

for i in num_list:
	if i % 2 != 1:
		num_list.remove(i)
print(num_list)