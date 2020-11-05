def fibonaci(n):
	x,y = 0,1

	while y < n:
		x,y = y,x+y
		print(y)
