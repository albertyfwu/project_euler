import fractions

res = []

for i in range(11, 100):
	for j in range(i + 1, 100):
		if i % 10 == 0 and j % 10 == 0:  # trivial example
			continue

		str_i = str(i)
		str_j = str(j)

		di1, di2 = str_i
		dj1, dj2 = str_j

		candidates = []
		if di2 == dj2:
			candidates.append((int(di1), int(dj1)))
		if di2 == dj1:
			candidates.append((int(di1), int(dj2)))
		if di1 == dj2:
			candidates.append((int(di2), int(dj1)))
		if di1 == dj1:
			candidates.append((int(di2), int(dj2)))

		valid = False

		for candidate in candidates:
			n, d = candidate
			if d == 0:
				continue
			if i * d == j * n:
				valid = True

		if valid:
			res.append((i, j))

final_n, final_d = 1, 1
for r in res:
	n, d = r
	final_n *= n
	final_d *= d

print final_d / fractions.gcd(final_n, final_d)