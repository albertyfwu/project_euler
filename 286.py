c = float(55)

def q(distance):
	return distance / c

def p(distance):
	return 1 - q(distance)

# use dynamic programming
# let w(pts, md) be probability of scoring
# pts points with 1 through md distances, inclusive
# w(pts, md) = w(pts, md - 1) * q(md) + w(pts - 1, md - 1) * p(md)
# w(0, md) = q(1) * q(2) * ... * q(md)
# w(pts, pts) = p(1) * p(2) * ... * p(pts)

max_distance = 50
max_pts = 20
w = []

def iterate():
	for i in range(0, max_pts + 1):
		w.append([0] * (max_distance + 1))

	# initialize
	w[0][0] = 1
	# initialize w(0, md)
	for j in range(1, max_distance + 1):
		w[0][j] = q(j) * w[0][j-1]
	# initialize w(pts, pts)
	for i in range(1, max_pts + 1):
		w[i][i] = p(i) * w[i-1][i-1]

	# compute
	for i in range(1, max_pts + 1):
		for j in range(i + 1, max_distance + 1):
			w[i][j] = w[i][j-1] * q(j) + w[i-1][j-1] * p(j)

	return w[20][50]

target = 0.02
err = 10**-15
a, b = float(max_distance), c
last_c = 100.0
# keep trying different c until w[20][50] is close to 2%
while True:
	# binary search for c in [a, b]
	c = (a + b) / 2
	ans = iterate()
	if ans > target:
		# increase range
		a = c
	elif ans < target:
		# decrease range
		b = c

	if abs(last_c - c) < err:
		print ans, last_c, c
		break
	else:
		last_c = c

	# if abs(target - ans) < err:
	# 	print ans, c
	# 	break