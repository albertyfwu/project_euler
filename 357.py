from itertools import chain, combinations
from operator import mul

def powerset(iterable):
  xs = list(iterable)
  # note we return an iterator rather than a list
  return chain.from_iterable( combinations(xs,n) for n in range(len(xs)+1) )

def prod(t):
	if len(t) == 0:
		return 1
	return reduce(mul, t)

def divisors(factors):
	for t in powerset(factors):
		yield prod(t)

def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

res = 0
print 'sieving'
primes = rwh_primes(10**8)
primes_set = set(primes)

def is_prime(n):
	if n == 2 or n == 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	return n in primes_set

count_mul = 1
print 'looping'
for prime in primes:
	if prime > count_mul * 10**6:
		print prime - 1
		count_mul += 1

	n = prime - 1
	iter_n = n
	primes_index = 0
	factors = []

	if 2 + n / 2 not in primes_set:
		continue
	# print n

	# find factors of n from the prime list
	success = True
	while iter_n > 1:
		# find the next prime
		p = primes[primes_index]
		if iter_n % p == 0:
			if iter_n % (p**2) == 0:
				success = False
				break
			factors.append(p)
			iter_n /= p
		primes_index += 1

	if success == False:
		continue

	# potential candidates
	ds = divisors(factors)
	# print n, ds
	success = True
	for d in ds:
		if not is_prime(d + n / d):
			success = False
			break
	if success:
		res += n

print res
