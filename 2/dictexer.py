dictionary = {'Arsen':10,'Davit':6,'Sargis':5,'Ani':2,'Hayk':4,'Davit':8,'Syuzanna':7,'Alis':9,'Armen':4,'Marta':7}
res = 0


# mijin tvabanakan

# for i in dictionary.values():
# 	res += i
# print(res/len(dictionary))

# for j in dictionary.values():
# 	if j > res:
# 		res = j


# for i in dictionary.keys():
# 	if dictionary[i] == res:
# 		print(i,res,end=',')  #maxy

# for k in dictionary.values():
# 	if k < res:
# 		res = k

# for i in dictionary.keys():
# 	if dictionary[i] == res:
# 		print(i,res,end=',') #miny

# for i,j in dictionary.items():
# 	if j > 5:
# 		print(i,j) # 5ic mecery

# for i,j in dictionary.items():
# 	if j < 5:
# 		print(i,j) # 5ic poqrer@

# name = input('enter name ')
# if name in dictionary.keys():
# 	print('yes have ')
# else:
# 	print('not')

# Milionaire
balance = 0
while True:
	harc1 = input('vor tvakanin e cnvel ? (1995/1996/1997/1998) ') == '1998'
	if harc1:
		print('duq vastakeciq 500 dram')
		balance += 500
		sharunakel = input('duq cankanum eq sharunakel? (y/n)')=='y'
	else:
		print('duq partveciq')
		break
	if not sharunakel:
		break

	harc2 = input('2+2*2 = ? (6/4/2/8)') == '6'
	if harc2:
		print('duq vastakeciq 5000 dram')
		balance += 4500
	else:
		print('duq partveciq')
		break
	harc3 = input('inchi e havasar armat 9@? (6/3/2/8) ') == '3'
	if harc3:
		print('duq vastakeciq 10.000 dram')
		balance += 5000
	else:
		print('duq partveciq')
		break
	harc4 = input('inch guyni e? (karmir/sev/spitak/dexin) ') == 'sev'
	if harc4:
		print('duq haxteciq dzer gumary kazmum e 20.000 dram')
		balance += 10000
		break
	else:
		print('duq partveciq dzer gumar@ kazmum e 0 dram')
		break