# class Year:
# 	def __init__(self,x):
# 		self.x = x

# 	def result(self):
# 		if self.x < 100:
# 			return 1

# 		elif self.x % 100 == 0:
# 			return self.x // 100
# 		else:
# 			res = self.x // 100 +1
# 			return res


# x = int(input('enter year '))
# result = Year(x)
# print(result.result())

# class Polidrom:
# 	def __init__(self,word):
# 		self.word = word

# 	def pol(self):
		
# 		return self.word == self.word[::-1]

# word = input('enter word ')
# res = Polidrom(word)
# print(res.pol())

# class Multy:
# 	def __init__(self,mylist):
# 		self.mylist = mylist

# 	def res(self):
# 		x = 0
# 		for i in range(len(self.mylist)-1):
# 			result = self.mylist[i] * self.mylist[i+1]
			
# 			if result > x:
# 				x = result
# 		return x


# mylist = [ 3,6,12,4,-1,-7,-3]
# resultMulty = Multy(mylist)
# print(resultMulty.res())

# class Word:
# 	def __init__(self,word):
# 		self.word = word

# 	def Length(self):
# 		C = max([len(i) for i in self.word])
# 		q = [i for i in self.word if len(i)  == C ]
# 		return q

# word = ['ads','asd','gas','sa','a']
# res = Word(word)
# print(res.Length())

class Lucky:
	def __init__(self,mylist):
		self.mylist = mylist

	def result(self):
		C = sum ([int(i) for i in str(self.mylist)[:len(str(self.mylist))//2]])
		q = sum ([int(i) for i in str(self.mylist)[len(str(self.mylist))//2:]])
		return C == q

mylist = 1230
res = Lucky(mylist)
print(res.result()) 


