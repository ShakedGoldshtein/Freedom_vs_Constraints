```python
def goldbach_representations(n):
    if n <= 2 or n % 2 != 0:
        return []

    def sieve(limit):
        sieve = [True] * (limit + 1)
        sieve[0] = sieve[1] = False
        for num in range(2, int(limit ** 0.5) + 1):
            if sieve[num]:
                sieve[num*num : limit+1 : num] = [False] * len(sieve[num*num : limit+1 : num])
        return sieve

    max_prime = n - 2
    is_prime = sieve(max_prime)
    primes = [i for i, prime in enumerate(is_prime) if prime]

    representations = []
    seen = set()

    for p in primes:
        q = n - p
        if q < p:
            break
        if is_prime[q] and p <= q and (p, q) not in seen:
            representations.append(f"{p}+{q}")
            seen.add((p, q))

    return representations
```