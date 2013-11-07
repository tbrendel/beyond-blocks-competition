"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def lpf(x):
	lpf = 2;
	while (x > lpf):
		if (x%lpf==0):
			x = x/lpf
			lpf = 2
		else:
			lpf+=1;
	print("Largest Prime Factor: %d" % (lpf));

def main():
	x = long(raw_input("Input long int:"))
	lpf(x);
	return 0;

if __name__ == '__main__':
    main()