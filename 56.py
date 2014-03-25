max_digit_sum = 0

for a in range(2, 100):
	for b in range(2, 100):
		n = a**b
		sum = 0
		for c in str(n):
			sum += int(c)
		max_digit_sum = max(max_digit_sum, sum)

print max_digit_sum