# sarqel dict u avelacnel keyn number listin
import json

# file_name = 'res.txt'

# name = ['Ani','Jon','Ben']
# number = [1,2,3]

# name_dict = {}

# c = -1
# for i in name:
# 	c += 1
# 	name_dict[number[c]] = i


# with open(file_name,'w') as f:
# 	json.dump(name_dict,f)

# with open(file_name) as f:
# 	name_load = json.load(f)
# 	print(name_load)

# song = 'song.txt'

# dictionar = {'addele hello':'Hallo for me every time i miss you where i am tired '}

# with open(song,'w') as f:
# 	json.dump(dictionar,f)


# with open(song) as f:	
# 	song_load = json.load(f)
# 	print(song_load['addele hello'])

# sum_mod3 = 'sum_mod.txt'

# def result(n):
# 	c = []
# 	for i in range(1,n):
# 		if i % 3 == 0 or i % 5 == 0:
# 			c.append(i)
# 	return sum(c)

# n = int(input('num = '))
# c = result(n)

# with open(sum_mod3,'w') as f:
# 	json.dump(c,f)

# with open(sum_mod3) as f:
# 	print(json.load(f))

vowel = 'vowel.txt'

def vowels(world):
	vowel = ('a','e','i','u','o')
	res = 0	
	for i in world:			
		if i in vowel:
			res += 1
	return res		

world = input('enter the world ')
js_vowel =vowels(world)
# print(js_vowel)

with open(vowel,'w') as f:
	json.dump(js_vowel,f)

with open(vowel) as f:
	print(json.load(f))