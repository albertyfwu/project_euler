def is_prime(n):
	if n == 1:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for factor in range(3, int(n**0.5) + 1):
		if n % factor == 0:
			return False
	return True

denominator = 5
numerator = 3

num = 9
incr = 4
while denominator < 10 * numerator:
	# print float(numerator) / denominator, incr
	denominator += 4
	for i in range(4):
		num += incr
		if is_prime(num):
			numerator += 1
	incr += 2

print incr - 1