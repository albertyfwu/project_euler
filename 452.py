import math
import operator

ARG = 10

def prod(l):
	return reduce(operator.mul, l)

def fact(n):
	# print 'fact', n
	if n == 0:
		return 1
	else:
		return n * fact(n-1)

def multi(top, bottoms):
	x = fact(top) / prod([fact(n) for n in bottoms])
	return x

def num_ways(used, arg):
	n = len(used)
	if n == 0:
		p = 1
	else:
		p = prod([(i+1)**used[i] for i in range(n)])
	rem = arg - sum(used)

	if rem == 0:
		ret = multi(arg, used)
		print used, ret
		# return 1
		return ret
	elif rem < 0:
		return 0

	# now we want to see what's the least number of n+1 we need in here so that n+2 doesn't exceed arg
	# we need to solve p * (n+1)^(x) * (n+2)^(rem-x) <= arg
	# => p * (n+2)^rem * (n+1)^x / (n+2)^x <= arg
	# => [(n+1)/(n+2)]^x <= arg / [p * (n+2)^rem]
	# => x = ceil[log(arg / [p * (n+2)^rem], (n+1)/(n+2))]
	min_n1 = max(int(math.ceil(math.log(arg / (p * float(n+2)**rem), (n+1) / float(n+2)))), 0)
	return sum([num_ways(used + [i], arg) for i in range(min_n1, arg + 1)])

print num_ways([], ARG)