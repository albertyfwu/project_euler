best_count = 0
best_p = None

for p in range(120, 1001):
	print p
	# a, b, p - (a + b)
	# greatest c can be is p / 2
	count = 0

	for a in range(2, p / 3):
		for b in range(a + 1, (p - a) / 2 + 1):
			c = p - a - b
			if a**2 + b**2 == c**2:
				count += 1

	if count > best_count:
		best_p, best_count = p, count

print best_p