from fractions import gcd
from fractions import Fraction

D = 1000000

best = Fraction(2, 5)

for d in range(8, 1000001):
	print d
	if (3 * d) % 7 == 0:
		n = 3 * d / 7 - 1
	else:
		n = 3 * d / 7
	best = max(best, Fraction(n, d))

print best