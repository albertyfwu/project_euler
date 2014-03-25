# 9^21 has 21 digits

count = 0
for e in range(1, 22):
	for b in range(1, 10):
		if len(str(b**e)) == e:
			count += 1

print count