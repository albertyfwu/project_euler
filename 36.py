def is_palindrome(s):
	length = len(s)
	for i in range(length):
		if s[i] != s[length - 1 - i]:
			return False
	return True

ret = 0

for i in range(1000000):
	base_10 = str(i)
	if not is_palindrome(base_10):
		continue

	base_2 = bin(i)[2:]
	if not is_palindrome(base_2):
		continue

	ret += i

print ret