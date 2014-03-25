from fractions import Fraction

def get_term(i):
	if i == 0:
		return 2
	r = i % 3
	if r != 2:
		return 1
	else:
		return (i + 1) / 3 * 2

n = 99

term = Fraction(get_term(n), 1)
for i in range(n - 1, -1, -1):
	term = get_term(i) + 1 / term

print sum([int(c) for c in str(term.numerator)])