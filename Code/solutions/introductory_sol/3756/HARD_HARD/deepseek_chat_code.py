```python
def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def get_goldbach_representations(n):
    if n % 2 != 0 or n <= 2 or n >= 32000:
        return []
    
    primes = generate_primes(n)
    prime_set = set(primes)
    representations = []
    
    for p in primes:
        if p > n // 2:
            break
        if (n - p) in prime_set:
            representations.append(f"{p}+{n-p}")
    
    return representations
```