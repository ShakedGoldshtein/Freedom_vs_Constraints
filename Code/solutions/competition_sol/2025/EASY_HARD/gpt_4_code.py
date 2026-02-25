```python
def solve(n):
    result, primes = [], [True] * (n+1)
    for p in range(2, n + 1):
        if primes[p]:
            result.append(p)
            for i in range(p * p, n + 1, p):
                primes[i] = False
    return len(result), result
```