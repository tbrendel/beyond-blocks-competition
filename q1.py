def q1(N):
	a = [ ]
	for i in range (3, N):
		if i%3 == 0 or i%5 == 0:
			a.append(i)
	return sum(a)