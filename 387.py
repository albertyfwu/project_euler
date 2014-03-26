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