file_name = 'name.txt'

with open(file_name,'w') as f:
	f.write('hi my friend\n what are you doing')

with open(file_name) as file:
	# print(file.readlines())
	for i in file:
		print(i)

c = open(file_name)
print(c.read())
c.close()