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
	ret = 1
	for t in xrange(1, min(k, n - k) + 1):
		ret *= (n + 1 - t)
		ret /= t
	return ret

count = 0
num_times = 0

def num_ways(used_len, used_prod, used_sum, used_multi, arg, m):
	global count 
	global num_times
	num_times += 1
	# start_t = time.time()
	# n = len(used)
	n = used_len
	p = used_prod

	rem = arg - used_sum

	if rem == 0:
		ret = used_multi
		return ret

	# now we want to see what's the least number of n+1 we need in here so that n+2 doesn't exceed arg
	# we need to solve p * (n+1)^(x) * (n+2)^(rem-x) <= arg
	# => p * (n+2)^rem * (n+1)^x / (n+2)^x <= arg
	# => [(n+1)/(n+2)]^x <= arg / [p * (n+2)^rem]
	# => x = ceil[log(arg / [p * (n+2)^rem], (n+1)/(n+2))]
	start_t = time.time()
	min_n1 = max(int(math.ceil(math.log(arg / float(p * (n+2)**rem), (n+1) / float(n+2)))), 0)
	end_t = time.time()
	count += end_t - start_t
	ret = sum([num_ways(n + 1, used_prod * (n + 1)**i, used_sum + i, (used_multi * binomial(used_sum + i, i)) % m, arg, m) 
		for i in range(min_n1, arg - used_sum + 1)])
	return ret

start = time.time()

initialize_factorials()
print num_ways(0, 1, 0, 1, ARG, MOD)

end = time.time()
print end - start, count, count / (end - start), num_times, (end - start) / num_times