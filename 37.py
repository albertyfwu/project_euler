# a truncatable prime contains a truncatable prime within it
# must contain [3, 7] as last digit and [2, 3, 5, 7] as first digit

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

# construct a truncatable prime from the right side
# keep checking that it's truncatable from the left

res = 0

count = 0
appends = [1, 2, 3, 5, 7, 9]
candidates = [3, 7]

while count < 11:
	candidate = candidates.pop(0)
	if is_prime(candidate):
		# test that the prime is right-truncatable
		is_right_truncatable = True
		str_candidate = str(candidate)
		for i in range(len(str_candidate)):
			new_candidate = int(str_candidate[:(i+1)])
			if not is_prime(new_candidate):
				is_right_truncatable = False
				break

		if is_right_truncatable and candidate > 10:
			res += candidate
			count += 1

		# append new candidates
		for append in appends:
			new_candidate = int(str(append) + str(candidate))
			candidates.append(new_candidate)

print res