positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
positions = [pos - 1 for pos in positions]

res = 1

n = 1
index = 0
count = 0

while index < len(positions):
	str_n = str(n)
	next_count = count + len(str_n)
	if positions[index] in range(count, next_count):
		print positions[index], count, str_n[positions[index] - count]
		res *= int(str_n[positions[index] - count])
		index += 1
	count = next_count
	n += 1

print res