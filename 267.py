# if you bet f, you end up with
# 1 + 2f if you win
# 1 - f if you lose
# find the value of f that corresponds to the lowest H such that
# (1 + 2f)^H * (1 - f)^(1000-H) >= 1 billion

import math

def g(x):
	return math.log(10**9/(1-x)**1000) / math.log((1+2*x)/(1-x))

# we need to solve the following function for 0:
def f(x):
	a = 3 * math.log(10**9 / (x-1)**1000)
	b = 2 * x + 1
	c = math.log(b / (1 - x))
	numerator = a - 1000 * b * c
	denominator = (x - 1) * b * c**2
	return numerator / denominator

def f_prime(f):
	def compute(x, dx):
		return (f(x+dx) - f(x)) / dx
	return compute

def root(f, x, dx = 0.01, tolerance=10**-20):
	df = f_prime(f)
	while True:
		x1 = x - f(x) / df(x, dx)
		t = abs(x1 - x)
		if t < tolerance:
			break
		x = x1
	return x

x = root(f, 0.15)
H = int(math.ceil(g(x)))

# H = 432
# calculate probabilities for heads of H through 1000 out of 1000

# let p[heads][flips] = prob. of 'heads' heads in 'flips' flips
# initialize the table
p = []
for i in range(0, 1000 + 1):
	p.append([0] * (1000 + 1))

# p[i][j] = p[i][j-1] * 1/2 + p[i-1][j-1] * 1/2
# p[0][0] = 1; p[0][j] = 1/2 * p[0][j-1]
# p[i][i-1] = 0

p[0][0] = 1.0
for j in range(1, 1000 + 1):
	p[0][j] = p[0][j-1] / 2
 
for i in range(1, 1000 + 1):
	p[i][i-1] = 0.0

for i in range(1, 1000 + 1):
	for j in range(i, 1000 + 1):
		p[i][j] = (p[i][j-1] + p[i-1][j-1]) / 2

res = 0
for heads in range(H, 1000 + 1):
	res += p[heads][1000]

print res