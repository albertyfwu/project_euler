# how many ways to add up to 200 if we have coins of values
# 1, 2, 5, 10, 20, 50, 100, 200?

all_values = [200, 100, 50, 20, 10, 5, 2, 1]

def num_ways(total, values):
	if total == 0:
		return 1
	if len(values) == 0:  # total != 0
		return 0

	ret = 0
	first_value, other_values = values[0], values[1:]

	while total >= 0:
		ret += num_ways(total, other_values)
		total -= first_value

	return ret

print num_ways(200, all_values)