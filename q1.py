def q1():
	a = [ ]
	for i in range (3,1001):
		if i%3 == 0 or i%5 == 0:
			a.append(i)
	return sum(a)