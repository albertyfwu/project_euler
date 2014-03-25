from fractions import Fraction

def check_frac(f):
	return len(str(f.numerator)) > len(str(f.denominator))

def run():
	count = 0
	term = Fraction(1, 1)
	for i in range(1000):
		term = 1 + Fraction(1, 1 + term)
		if check_frac(term):
			count += 1
	return count

print run()