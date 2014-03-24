def cycle_length(d):
	# cycle length for 1 / d
	remainder_position = {}

	position = 0
	value = 1

	while value not in remainder_position and value != 0:
		remainder_position[value] = position
		value = (value * 10) % d
		position += 1

	if value == 0:
		return 0

	return position - remainder_position[value]

best_d = None
best_cycle = 0

for d in range(2, 1000):
	cycle = cycle_length(d)
	if cycle > best_cycle:
		best_d, best_cycle = d, cycle

print best_d, best_cycle