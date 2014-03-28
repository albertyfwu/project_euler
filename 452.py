"""Taken from ProjectEuler forum"""

ARG = 10**9

def F(m, n, mod):
   def rec(k, product, combs, slotsLeft, result, skip):
      if product*k > m:
         return
      powK, q = k, 1
      if k > 1:
         c = slotsLeft
         while powK*product <= m:
            result[0] = (result[0] + c*combs)%mod
            rec(k+1, product*powK, (combs*c)%mod, slotsLeft-q, result, False)
            q += 1
            powK *= k
            c = c*(slotsLeft-q+1)/q
      if not skip:
         limit = int((m/product)**0.5)+1
         for i in xrange(k+1, limit):
            rec(i, product, combs, slotsLeft, result, True)
         result[0] = (result[0] + max(0, combs*slotsLeft*(m/product - max(k+1, limit) + 1)))%mod
   result = [1]
   rec(1, 1, 1, n, result, False)
   return result[0]

print F(ARG, ARG, 1234567891)