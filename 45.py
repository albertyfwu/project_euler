# if triangle number is x, then 
# for pentagonal, we have n = (1/6) * (sqrt(24x+1) + 1)
# for hexagonal, we have n = (1/4) * (sqrt(8x+1) + 1)

k = 285
while True:
	k += 1
	x = k * (k + 1) / 2
	# check pentagonal
	sqrt = (24 * x + 1)**0.5
	if abs(sqrt - int(sqrt)) > 0.00001:
		continue
	if (int(sqrt) + 1) % 6 != 0:
		continue
	# check hexagonal
	sqrt = (8 * x + 1)**0.5
	if abs(sqrt - int(sqrt)) > 0.00001:
		continue
	if (int(sqrt) + 1) % 4 != 0:
		continue
	# it works!
	print k, x
	break