n_pete = [0] * 36
n_colin = [0] * 36

def populate(n_arr, num_dice, num_sides):
	def sub(n_arr, rolls):
		if len(rolls) == num_dice:
			n_arr[sum(rolls) - 1] += 1
		else:
			for i in range(1, num_sides + 1):
				sub(n_arr, rolls + [i])

	sub(n_arr, [])

populate(n_pete, 9, 4)
populate(n_colin, 6, 6)

total = sum(n_pete) * sum(n_colin) # total outcomes

count = 0
for i in range(1, 36):
	for j in range(0, i):
		count += n_pete[i] * n_colin[j]

print count, total, float(count) / total