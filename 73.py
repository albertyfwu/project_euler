# iterate over possible numerators, 2 through 6000
# search denominators that are relatively prime

from fractions import gcd

D = 12000

count = 0
for n in range(2, D / 2):
	print n
	for d in range(2 * n + 1, min(3 * n, D) + 1):
		if gcd(n, d) == 1:
			count += 1
			# print n, d

print count