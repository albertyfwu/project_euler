def num_distinct_prime_factors(n):
	ret = 0
	old_n = n
	sqrt_n = int(n**0.5)
	for factor in range(2, sqrt_n + 1):
		if n % factor == 0:
			ret += 1
			if ret == 4:
				return ret
			# divide it out
			while n % factor == 0:
				n /= factor
	if n == 1:
		return ret
	else:
		return ret + 1

streak = 0
n = 647

while True:
	if streak == 4:
		print n - 4
		break
	if num_distinct_prime_factors(n) >= 4:
		streak += 1
	else:
		streak = 0
	n += 1