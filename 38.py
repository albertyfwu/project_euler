# integer x is 9000 format, times 1 and times 2, n = 2

def is_pandigital(n):
	s = set()
	for c in str(n):
		d = int(c)
		s.add(d)
	return sum(s) == 45

largest_pandigital = 918273645

for i in range(9183, 10000):
	prod1 = i * 1
	prod2 = i * 2
	n = int(str(prod1) + str(prod2))
	if not is_pandigital(n):
		continue
	largest_pandigital = max(largest_pandigital, n)

print largest_pandigital