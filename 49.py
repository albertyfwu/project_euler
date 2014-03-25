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

def are_anagrams(n1, n2, n3):
	n1_c = set()
	for c in str(n1):
		n1_c.add(c)
	n2_c = set()
	for c in str(n2):
		n2_c.add(c)
	n3_c = set()
	for c in str(n3):
		n3_c.add(c)
	return n1_c == n2_c and n2_c == n3_c

def run():
	primes = []
	for n in range(1001, 10000, 2):
		if is_prime(n):
			primes.append(n)

	primes_set = set(primes)

	for i in range(len(primes)):
		prime = primes[i]
		# print prime
		j = 2
		while prime + 2 * j < 10000:
			n1 = prime
			n2 = prime + j
			n3 = prime + 2 * j
			# print n1,n2,n3
			if n1 not in primes_set:
				j += 2
				continue
			if n2 not in primes_set:
				j += 2
				continue
			if n3 not in primes_set:
				j += 2
				continue
			if not are_anagrams(n1, n2, n3):
				j += 2
				continue
			print n1, n2, n3
			break

run()