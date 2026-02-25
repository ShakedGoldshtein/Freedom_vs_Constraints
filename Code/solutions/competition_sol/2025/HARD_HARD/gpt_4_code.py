```python
def solve(n):
    is_prime = [1 for _ in range(n+1)]
    smallest_prime = [i % 2 for i in range(n+1)]
    smallest_prime[1] = smallest_prime[0] = 0
    smallest_prime[2] = 2
    is_prime[1] = is_prime[0] = 0
    is_prime[2] = 1

    for p in range(3, int(n ** 0.5) + 1, 2):
        if is_prime[p]:
            smallest_prime[p] = p
            for i in range(p * p, n + 1, p):
                if is_prime[i]:
                    smallest_prime[i] = p
                    is_prime[i] = 0            

    for p in range(3, n + 1, 2):
        if is_prime[p]:
            smallest_prime[p] = p

    primes = [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        prime_factors = []
        x = i
        while x > 1:
            prime_factors.append(smallest_prime[x])
            x //= smallest_prime[x]
        for factor in prime_factors:
            if primes[factor] < prime_factors.count(factor):
                primes[factor] = prime_factors.count(factor)

    numbers = []
    for i in range(2, len(primes)):
        for _ in range(primes[i]):
            numbers.append(i ** (primes[i]))
            primes[i] -= 1

    return len(numbers), numbers
                
```
