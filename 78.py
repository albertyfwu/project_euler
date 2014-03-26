def g(k):
	return k * (3 * k - 1) / 2

def G(k):
	# 1 => 1
	# 2 >= -1
	# 3 >= 2
	# 4 >= -2
	# 5 >= 3
	# 6 >= -3
	if k % 2 == 1:
		return g((k + 1) / 2)
	else:
		return g(-k / 2)

def sign(k):
	# 1, 2 => 1; 3, 4 => -1
	if k % 4 in [1, 2]:
		return 1
	else:
		return -1

p = [1, 1, 2, 3, 5]

n = 5
while True:
	res = 0

	i = 1
	offset = G(i)
	s = sign(i)
	offset = G(i)
	while n - offset >= 0:
		res += s * p[n - offset]
		i += 1
		s = sign(i)
		offset = G(i)

	p.append(res)
	n += 1

	if res % 10**6 == 0:
		print n-1
		break