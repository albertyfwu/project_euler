# triangle numbers are of form n(n+1)/2
# n = p1^e1 * p2^e2 * ...
# n+1 = q1^f1 * q2^f2 * ...

def num_divisors(n):
	# get prime factorization
	total_divisors = 1
	sqrt_n = int(n**0.5)
	factor = 2
	while factor <= sqrt_n:
		e = 0
		# find out how many times factor goes into n
		while True:
			if n % factor != 0:
				break
			n /= factor
			e += 1
		total_divisors *= (e + 1)
		factor += 1

	# remaining part is prime
	if n == 1:
		return total_divisors
	else:
		return 2 * total_divisors

n = 1
while True:
	num = n * (n+1) / 2
	if num_divisors(num) > 500:
		break
	n += 1

print num