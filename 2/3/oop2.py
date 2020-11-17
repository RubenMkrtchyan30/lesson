# class Person:
# 	def __init__(self,age,name,surname):
# 		self.name = name
# 		self.age = age
# 		self.surname = surname

# 	def result(self):
# 		print(self.name, self.surname)

# class Women(Person):
# 	def __init__(self,age,name,surname,lif):
# 		super().__init__(age,name,surname)
# 		self.lif = lif
# 	def res(self):
# 		return self.lif
		
# 	def res_women(self):
# 		 print(self.age,self.name,self.surname,self.lif)


# class Man(Person):
# 	def __init__(self,age,name,surname,hasak):
# 		Person.__init__(self,age,name,surname)
# 		self.hasak = hasak

# 	def res_man(self):
# 		print(self.age,self.name,self.surname,self.hasak)

# y = Man('20','Dav','Sargsyan','201')

# x = Women('20','Ani','Sargsyan','21')
# print(x.res())
# x.res_women()
# y.res_man()

# class Armenia:
# 	def country(self):
# 		print('Erevan')


# class Usa:
# 	def country(self):
# 		print('Glendale')

# country_Arm = Armenia()
# country_Usa = Usa()
# country_Arm.country()
# country_Usa.country()

# class Number1:
# 	def __init__(self,num1,num2):
# 		self.num1 = num1
# 		self.num2 = num2


# 	def string(self):
# 		print(str(self.num1) + str(self.num2))

# 	def res(self):
# 		print(self.num1 + self.num2)


# Num = Number1(5,1)

# Num.res()
# Num.string()

class Maxlist:
	def __init__(self,number):
		self.number = number

	def maxl(self):
		x = 0
		for i in self.number:
			if i > x:
				x = i
		print(x)

number = [4,5,12,46]
x = Maxlist(number)
x.maxl()