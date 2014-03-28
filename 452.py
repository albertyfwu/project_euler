import math

ARG = 4

def num_ways(used, arg):
	n = len(used)
	if n == 0:
		p = 1
	else:
		p = sum([(i+1)**used[i] for i in range(n)])
	rem = arg - sum(used)

	if rem == 0:
		return 1  # fix later
	elif rem < 0:
		return 0

	# now we want to see what's the least number of n+1 we need in here so that n+2 doesn't exceed arg
	# we need to solve p * (n+1)^(x) * (n+2)^(rem-x) <= arg
	# => p * (n+2)^rem * (n+1)^x / (n+2)^x <= arg
	# => [(n+1)/(n+2)]^x <= arg / [p * (n+2)^rem]
	# => x = ceil[log(arg / [p * (n+2)^rem], (n+1)/(n+2))]
	min_n1 = int(math.ceil(math.log(arg / (p * float(n+2)**rem), (n+1) / float(n+2))))
	return sum([num_ways(used + [i], arg) for i in range(min_n1, arg + 1)])

print num_ways([], ARG)