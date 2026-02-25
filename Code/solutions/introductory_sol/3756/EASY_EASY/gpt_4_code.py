```python
def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while p ** 2 <= n:
        if primes[p] is True:
            for i in range(p ** 2, n+1, p):
                primes[i] = False
        p += 1
    primes = [p for p in range(2, n) if primes[p]]
    return primes

def goldbach_pairs(n):
    if n % 2 != 0:
        return []
    primes = sieve_of_eratosthenes(n)
    pairs = []
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if primes[i] + primes[j] == n:
                pairs.append(f'{primes[i]}+{primes[j]}')
    return pairs
```