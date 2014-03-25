# pandigital combination would be 1-digit times 4-digit or 2-digit times 3-digit

def is_pandigital(i, j, product):
	digits = set()
	for s in [str(i), str(j), str(product)]:
		for c in s:
			d = int(c)
			digits.add(d)
	return sum(digits) == 45

pandigitals = set()

for i in range(2, 100):
	# if 1-digit, only do 4 digits; if 2-digit, only do 3-digits
	if i < 10:
		begin = 1234
	else:
		begin = 123
	end = 10000 / i + 1

	for j in range(begin, end):
		product = i * j
		if is_pandigital(i, j, product):
			pandigitals.add(product)

print sum(pandigitals)