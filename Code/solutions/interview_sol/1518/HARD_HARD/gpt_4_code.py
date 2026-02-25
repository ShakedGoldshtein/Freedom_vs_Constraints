```python
def sieveOfEratosthenes(n):
    primes = [True for i in range(n+1)]
    primes[0] = primes[1] = False
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return primes

def solve(T, test_cases):
    prime_sieve = sieveOfEratosthenes(1e5)
    prime = [i for i in range(2, len(prime_sieve)) if prime_sieve[i]]

    results = []
    for _ in range(T):
        N, K = test_cases[_]
        if K > N:
            results.append(0)
            continue
        if K == 1:
            if prime_sieve[N]:
                results.append(1)
            else:
                results.append(0)
            continue
        if K == 2:
            if N % 2 == 0 and N > 2:
                results.append(1)
            elif N-2 in prime:
                results.append(1)
            else:
                results.append(0)
            continue
        if N >= K*2:
            results.append(1)
        else:
            results.append(0)
    return results
```
