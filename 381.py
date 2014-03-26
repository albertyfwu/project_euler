def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes:
        return True
    if n in (0, 1):
    	return False
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

# if p is prime, we know that
# (p-1)! = -1 (mod p)
# (p-2)! = 1 (mod p)
# (p-3)! = (p - 1) / 2 (mod p)
# 6 * (p-4)! = 1 (mod p)
# 24 * (p-5)! = -1 (mod p)

# last two give us 24 * sum = 3 => 8 * sum = 1 (mod p)

# total give us 24 * sum = -24 + 24 - 12 + 4 - 1 = -9
# => 8 * sum = -3 (mod p)
# p = 1 mod 8: sum = (3 * p - 3) / 8
# p = 3 mod 8: sum = (9 * p - 3) / 8
# p = 5 mod 8: sum = (7 * p - 3) / 8
# p = 7 mod 8: sum = (5 * p - 3) / 8

def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

N = 10**8
print 'sieving'
primes = rwh_primes(N)[2:]

print 'computing'
res = 0
p_index = 0
for n in range(5, N):
    if n % (N / 100) == 0:
        print n
    if p_index == len(primes):
        break
    if n != primes[p_index]:
        continue
    p_index += 1
    r = n % 8
    s = (((r * 3) % 8) * n - 3) / 8
    res += s % n

print res