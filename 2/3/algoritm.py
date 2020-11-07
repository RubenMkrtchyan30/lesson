# def recursion():
# 	print('hello world')
# 	recursion()
# recursion()

# def factorial(x):
# 	if x ==0:
# 		return 1
# 	elif x ==1:
# 		return 1
# 	else:
# 		return x*factorial(x-1)
# print(factorial(5))

# def fibonacci(x):
# 	if x == 1:
# 		return 0
# 	elif x == 2:
# 		return 1
# 	else:
# 		return fibonacci(x-1) + fibonacci(x-2)
# print(fibonacci(5))

# old_list = [12,56,87,54,21,365,45,17]

# def bubble_sort(my_list):
# 	last_item = len(my_list) -1

# 	for i in range(0,last_item):
# 		for j in range(0,last_item-i):
# 			if my_list[j]>my_list[j+1]:
# 				my_list[j],my_list[j+1] = my_list[j+1],my_list[j]

# 			print(my_list)
# 	return my_list


# print('old list',old_list)
# new_list = bubble_sort(old_list).copy()
# print('New list',new_list)

# a = 144
# b = 74
# c = 327

# if a > b > c:
# 	a,b,c = c,b,a
# 	print(a,b,c)

# elif a>c>b:
# 	a,b,c=b,c,a
# 	print(a,b,c)

# elif b > a > c:
# 	a,b,c=c,a,b
# 	print(a,b,c)

# elif b>c>a:
# 	a,b,c=a,c,b
# 	print(a,b,c)


# elif c>b>a:
# 	a,b,c=a,b,c
# 	print(a,b,c)

# elif c>a>b:
# 	a,b,c=b,a,c
# 	print(a,b,c)

# else:
# 	print(a,b,c)

list1 = [1,2,5,-36,-33,34]
num = -35
sort = list1[1] - num
res = 0

for i in list1:
	if i - num < sort:
		sort = i -num
		res = i[]

	print(res)
