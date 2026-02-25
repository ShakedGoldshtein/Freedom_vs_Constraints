```python
from fractions import Fraction

def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return primes

def solve(t, nums):
    primes = sieve(max(nums)*2)
    results = []
    for n in nums:
        lower_prime = next(x for x in range(n,0,-1) if primes[x])
        upper_prime = next(x for x in range(n+1,len(primes)) if primes[x])
        results.append(Fraction(1,lower_prime*upper_prime))
    return results
```