# only need to search for primes up until 1000000 / 21 = 47619

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

primes = []

for i in range(2, 47619):
	if is_prime(i):
		primes.append(i)

num_primes = len(primes)

best_consec = 1
best_prime = None

curr_index = 0
iter_index = 0
curr_sum = 0
while curr_index < num_primes:
	next_sum = curr_sum
	next_sum += primes[iter_index]
	iter_index += 1

	if next_sum > 1000000 or curr_index > 1000000 / best_consec:
		curr_index += 1
		iter_index = curr_index
		curr_sum = 0
		continue

	# otherwise, continue adding
	if is_prime(next_sum):
		curr_streak = iter_index - curr_index
		if curr_streak > best_consec:
			best_consec, best_prime = curr_streak, next_sum

	curr_sum = next_sum

print best_consec, best_prime