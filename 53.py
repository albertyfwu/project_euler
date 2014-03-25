# when n = 2k, (2k, k) is maximal. keep moving left until 
# when n = 2k + 1, (2k+1, k) = (2k+1, k+1) are maximal

count = 4 # for 23, we have 23 C 10 through 23 C 13
last_k = 10
last_binomial = 1144066 # 23 C 10
for n in range(24, 101):
	iter_k = last_k
	new_binomial = last_binomial * n / (n - iter_k)
	# (n, k-1) / (n, k) = k / (n + 1 - k)
	# keep multiplying by this until new_binomial is less than 10**6
	while True:
		next_binomial = new_binomial * iter_k / (n + 1 - iter_k)
		if next_binomial > 1000000:
			iter_k -= 1
			new_binomial = next_binomial
		else:
			break

	# compute number from iter_k to n - iter_k
	# that's n - 2 * iter_k + 1
	count += (n - 2 * iter_k + 1)
	last_k = iter_k
	last_binomial = new_binomial

print count