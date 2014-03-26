def collatz_step(n):
	r = n % 3
	if r == 0:
		return 'D', n / 3
	elif r == 1:
		return 'U', (4 * n + 2) / 3
	else:
		return 'd', (2 * n - 1) / 3

# match_seq = 'DdDddUUdDD'
match_seq = 'UDDDUdddDDUDDddDdDddDDUDDdUUDd'
len_match_seq = len(match_seq)

def run():
	n = 10**15
	# n = 10**6
	while True:
		n += 1
		if n % 10**5 == 0:
			print n
		count = 0
		iter_n = n
		while iter_n != 1:
			c, iter_n = collatz_step(iter_n)
			count += 1
			if c != match_seq[count - 1]:
				break
			if count == len_match_seq:
				return n

print run()
