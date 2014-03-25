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

def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def is_square(n):
	return isqrt(n)**2 == n

primes = []

n = 1
while True:
	n += 2
	if is_prime(n):
		primes.append(n)
	else:
		# it's an odd composite
		valid = False
		for prime in primes:
			if is_square((n - prime) / 2):
				valid = True
				break
		if not valid:
			print n
			break