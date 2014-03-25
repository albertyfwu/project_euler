count = 0

def w(pos, prev, length, start, end, cache = {}):
	global count
	if (length) == 40:
		count += 1

	# print pos, prev, length, start, end
	tup = (pos, prev, length, start, end)
	if tup in cache:
		return cache[tup]

	if pos == length:
		if (start, end) == (0, 9):
			return 1
		else:
			return 0
	else:
		if prev < 9:
			w1 = w(pos + 1, prev + 1, length, start, max(end, prev + 1), cache)
		else:
			w1 = 0
		if prev > 0:
			w2 = w(pos + 1, prev - 1, length, min(start, prev - 1), end, cache)
		else:
			w2 = 0
		cache[tup] = w1 + w2
		return w1 + w2

res = 0
for l in range(10, 41):
	for i in range(1, 10):
		res += w(1, i, l, i, i)

print res
print count