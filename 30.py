# let's get an upper bound
# for d-digit number, it is between 10^(d-1) and 10^d
# sum of fifth powers of digits is at most d * 9^5 = d * 59049
# we need to find d where d * 59049 not large enough to exceed 10^(d-1)
# d = 7 does the trick
# we don't need to search above 
# in fact, searching up to 249,999 is good enough

ret = 0

for n in range(2, 250000):
	sum_fifths = 0
	for c in str(n):
		d = int(c)
		sum_fifths += d**5
	if n == sum_fifths:
		ret += n

print ret