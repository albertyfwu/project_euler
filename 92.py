a = set() # end at 1
b = set() # end at 89

def sort_digits_strip_zeros(n):
	return int(''.join(sorted(str(n))).replace('0', ''))

count = 0

for n in range(1, 10*10**6):
	cycle = set()
	iter_n = n
	while iter_n not in [1, 89]:
		sorted_n = sort_digits_strip_zeros(iter_n)
		cycle.add(sorted_n)
		if sorted_n in a:
			a.update(cycle)
			break
		if sorted_n in b:
			b.update(cycle)
			count += 1
			break
		new_num = 0
		for c in str(iter_n):
			d = int(c)
			new_num += d**2
		iter_n = new_num
	if iter_n == 1:
		a.update(cycle)
	elif iter_n == 89:
		b.update(cycle)
		count += 1

print count