nahanj = int(input('mutqagreq taretivy '))
payman1 = nahanj % 4 == 0
payman2 = nahanj % 100 == 0
payman3 = nahanj % 400 != 0
if payman3 or payman1 and payman2:
	print('nahanj tari e ')
else:
	print('nahanj che ')