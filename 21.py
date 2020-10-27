import random as r


print('Hi guys you play 21. game ')

players_choice = 'u p'
result_choice = r.choice(players_choice) == 'u'
point = 0

while True:
	
	if players_choice:
		
		if point > 20:
			break

		first_choice = input('\n\t1,2,3 ')
		
		if first_choice.isdigit():
			first_choice = int(first_choice)
		
			if 0 < first_choice < 4:
				
				print(point,'+',first_choice,'=',point+ first_choice)
				point += first_choice

				if point >= 17:
					pc_point = 20 - point
					first_choice = 1
					print(point,'+',pc_choice,'=',point+pc_choice)
					print('you lose ',21)
					break
			

				pc_choice = r.randint(1,3)
				print(point,'+',pc_choice,'=',point+pc_choice)
				point += pc_choice



			else:
				print('please input number 1-3 ')
		
		else:		
			print('\n\t is not digit')