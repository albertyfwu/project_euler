loop_lengths = {}

for num in [169, 363601, 1454, 169]:
	loop_lengths[num] = 3

for num in [871, 45361]:
	loop_lengths[num] = 2

for num in [872, 45362]:
	loop_lengths[num] = 2

for num in [1, 2, 145]:
	loop_lengths[num] = 1

factorials = [1]
def init_factorials():
	for i in range(1, 10):
		factorials.append(i * factorials[-1])

def sum_factorials(n):
	return sum([factorials[int(c)] for c in str(n)])

init_factorials()

count = 0

for n in range(10**6):
	history = []
	iter_n = n
	last_n = None
	while iter_n not in loop_lengths:
		if iter_n == last_n:
			loop_lengths[iter_n] = 1
			break
		history.append(iter_n)
		last_n = iter_n
		iter_n = sum_factorials(iter_n)
	if len(history) > 0 and history[-1] == iter_n:
		chain_length = len(history)
	else:
		chain_length = len(history) + loop_lengths[iter_n]
	for i in range(len(history)):
		loop_lengths[history[i]] = chain_length - i
	if chain_length == 60:
		count += 1

print count