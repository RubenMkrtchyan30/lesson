import json
# file_name = 'test.json'

# player1 = {
# 	'name' : 'Aram',
# 	'age' : 18,
# 	'height' : 180,
# 	'awards' : ['master',3,2,1]
# }

# player2 = {
# 	'name' : 'Ani',
# 	'age' : 17,
# 	'height' : 183,
# 	'awards' : [3,2,1]
# }

# myplayers = [player1,player2]
# with open(file_name, 'w') as file:
# 	json.dump(myplayers,file)

# file = open(file_name)#fayl kardum e
# json_data = json.load(file)
# for data in json_data:
# #	print(data)#mer tvyalnern e het berum

# 	print('\nPlayer name is ',data['name'])
# 	print('Player age is',data['age'])
# 	print('Player heiht is',data['height'])
# 	print('Player awards is',data['awards'])
	
# file_name = 'users_1.txt'

# try:
# 	with open(file_name) as file:
# 		user=json.load(file)
# 		print('hello',user)

# except:
# 	username = input('what is your name? ')
# 	with open(file_name,'w') as file:
# 		user = json.dump(username,file)

user = 'user.json'

# vayr = input('vortex eq uzum lvanal? ') == 'zeytun'
# if vayr:

# 	car_tipe = input('jeep or sedan')

# 	if car_tipe == 'jeep':
# 		price = 1000

# 	else:
# 		price = 2000

# user_result = {
# 	'vayr':vayr,
# 	'car_tipe':car_tipe,
# 	'price':price
# }

try:
	with open(user) as file:
		user=json.load(file)
		print(user)

except:
	with open(user,'w') as file:
		result= json.dump(user_result,file)
