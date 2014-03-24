# sum like
# 1 (+2)
# 3, 5, 7, 9 (+4)
# 13, 17, 21, 25 (+6)
# 31, 37, 43, 49

NUM = 1001

ret = 1
incr = 2
count = 0
num = 1

while num != NUM**2:
	num += incr
	ret += num

	if count == 3:
		incr += 2

	count = (count + 1) % 4

print ret