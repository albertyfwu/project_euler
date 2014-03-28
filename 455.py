def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def exp(n, x, m, cache):
    # computes n^x (mod m) using fast exponentiation
    if x in cache:
        return cache[x]
    if x == 0:
        return 1
    half = exp(n, x / 2, m, cache)
    first = (half * half) % m
    if x % 2 == 0:
        ret = first
    else:
        ret = (first * n) % m
    cache[x] = ret
    return ret

# print modinv(4, 100)

# 4^5 = 24 (mod 100)
# 4^4 = 56 (mod 100)

m = 10**9
# a, b = 2, 10**3
a, b = 4, 4
for n in xrange(a, b + 1):
    # # pre-compute the modular inverse
    # inv = modinv(n, m)
    # calculate last 9 digits of n^x
    cache = {}
    for x in xrange(m-1, 0, -1):
        # print x
        # print len(cache)
        last9 = exp(n, x, m, cache)
        del cache[x]
        if last9 == x:
            print x
            break
