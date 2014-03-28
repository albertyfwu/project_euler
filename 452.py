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

def multi(top, bottoms):
	# biggest number will be the first one
	ret = 1
	largest = bottoms[0]
	for i in range(largest + 1, top + 1):
		ret *= i
	for i in range(1, len(bottoms)):
		ret /= fact(bottoms[i])
	return ret

count = 0

def num_ways(used, used_prod, used_sum, arg, m):
	global count 
	start_t = time.time()
	n = len(used)
	p = used_prod

	rem = arg - used_sum

	if rem == 0:
		ret = multi(arg, used) % m
		# ret = 1
		# print used, ret
		# return 1
		return ret

	# now we want to see what's the least number of n+1 we need in here so that n+2 doesn't exceed arg
	# we need to solve p * (n+1)^(x) * (n+2)^(rem-x) <= arg
	# => p * (n+2)^rem * (n+1)^x / (n+2)^x <= arg
	# => [(n+1)/(n+2)]^x <= arg / [p * (n+2)^rem]
	# => x = ceil[log(arg / [p * (n+2)^rem], (n+1)/(n+2))]
	# start_t = time.time()
	min_n1 = max(int(math.ceil(math.log(arg / (p * float(n+2)**rem), (n+1) / float(n+2)))), 0)
	end_t = time.time()
	count += end_t - start_t
	ret = sum([num_ways(used + [i], used_prod * (n + 1)**i, used_sum + i, arg, m) for i in range(min_n1, arg - used_sum + 1)])
	return ret

start = time.time()

initialize_factorials()
print num_ways([], 1, 0, ARG, MOD)

end = time.time()
print end - start, count, count / (end - start)