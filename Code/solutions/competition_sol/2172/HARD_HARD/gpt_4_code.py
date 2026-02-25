```python
from fractions import Fraction

def sieve(limit: int):
    primes = [True] * limit
    primes[0], primes[1] = False, False
    for ind, val in enumerate(primes):
        if val is True:
            primes[ind*2: limit: ind] = [False] * (((limit-1)//ind) - 1)
    return [ind for ind, val in enumerate(primes) if val is True]


def solve(t: int, test_cases: list):
    results = []
    primes = sieve(10**6 + 100)
    accum = [0]*(10**6 + 100)
    for i in range(1, 10**6 + 100):
        accum[i] = accum[i-1] + Fraction(1, primes[i-2]*primes[i-1])

    for i in range(t):
        n = test_cases[i]
        results.append(str(accum[n-2]))

    return results
```