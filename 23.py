def sum_of_divisors(n):
	# find the prime factorization
	orig_n = n
	ret = 1
	sqrt_n = int(n**0.5)
	p = 2
	while p <= sqrt_n:
		e = 0
		while True:
			if n % p != 0:
				break
			n /= p
			e += 1
		ret *= (p**(e+1) - 1) / (p - 1)
		p += 1

	# do we have any prime factor left over?
	if n != 1:
		ret *= (n + 1)

	return ret - orig_n

def is_abundant(n):
	return sum_of_divisors(n) > n

# find all the abundant numbers
abundant_numbers = set()
for n in range(12, 28123 + 1):
	if is_abundant(n):
		abundant_numbers.add(n)

# from the sum of all integers 1 through 28123,
# subtract all numbers that can be written
can_be_written = set()
for i in abundant_numbers:
	for j in abundant_numbers:
		s = i + j
		if s <= 28123:
			can_be_written.add(s)

print 28123 * (28123 + 1) / 2 - sum(can_be_written)