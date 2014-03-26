digits = [i for i in range(0, 10)]
rt_harshads = [i for i in range(1, 10)]

def sum_of_digits(n):
	return sum([int(c) for c in str(n)])

def is_harshad(n):
	return n % sum_of_digits(n) == 0

def is_strong_harshad(n):
	s = sum_of_digits(n)
	return n % s == 0 and is_prime(n / s)

def is_below_threshold(n):
	return n < 10**14

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes:
        return True
    if n in (0, 1):
    	return False
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

srt_harshad_primes = []

while len(rt_harshads) > 0:
	rt_harshad = rt_harshads.pop(0)
	if not is_below_threshold(rt_harshad):
		continue
	# let's see if it's a strong harshad, if we can form a prime
	if is_strong_harshad(rt_harshad):
		for d in digits:
			candidate = rt_harshad * 10 + d
			if is_below_threshold(candidate) and is_prime(candidate):
				srt_harshad_primes.append(candidate)
	# now let's generate rt harshads
	for d in digits:
		candidate = rt_harshad * 10 + d
		if is_harshad(candidate):
			rt_harshads.append(candidate)

print srt_harshad_primes, sum(srt_harshad_primes)