def is_palindrome(n):
	str_n = str(n)
	length = len(str_n)
	for i in range(length / 2):
		if str_n[i] != str_n[length - 1 - i]:
			return False
	return True

count = 0
for n in range(1, 10000):
	new_n = n
	is_lychrel = True
	for k in range(50):
		new_n = new_n + int(str(new_n)[::-1])
		if is_palindrome(new_n):
			is_lychrel = False
			break
	if is_lychrel:
		count += 1

print count
