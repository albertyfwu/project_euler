import math
import operator
import time

ARG = 10**2
MOD = 1234567891

def prod(l):
	return reduce(operator.mul, l)

fact_cache = []

def fact(n):
	if n <= 30:
		return fact_cache[n]
	return math.factorial(n)

def initialize_factorials():
	for i in range(0, 30):
		fact_cache.append(math.factorial(i))

def binomial(n, k):
	ntok = 1
	ktok = 1
	for t in xrange(1, min(k, n - k) + 1):
		ntok *= n
		ktok *= t
		n -= 1
	return ntok / ktok

count = 0

def num_ways(used, used_prod, used_sum, used_multi, arg, m):
	global count 
	start_t = time.time()
	n = len(used)
	p = used_prod

	rem = arg - used_sum

	if rem == 0:
		ret = used_multi
		end_t = time.time()
		count += end_t - start_t
		return ret

	# now we want to see what's the least number of n+1 we need in here so that n+2 doesn't exceed arg
	# we need to solve p * (n+1)^(x) * (n+2)^(rem-x) <= arg
	# => p * (n+2)^rem * (n+1)^x / (n+2)^x <= arg
	# => [(n+1)/(n+2)]^x <= arg / [p * (n+2)^rem]
	# => x = ceil[log(arg / [p * (n+2)^rem], (n+1)/(n+2))]
	min_n1 = max(int(math.ceil(math.log(arg / (p * float(n+2)**rem), (n+1) / float(n+2)))), 0)
	ret = sum([num_ways(used + [i], used_prod * (n + 1)**i, used_sum + i, (used_multi * binomial(used_sum + i, i)) % m, arg, m) 
		for i in range(min_n1, arg - used_sum + 1)])
	return ret

start = time.time()

initialize_factorials()
print num_ways([], 1, 0, 1, ARG, MOD)

end = time.time()
print end - start, count, count / (end - start)