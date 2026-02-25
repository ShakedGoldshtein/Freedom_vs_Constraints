```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def solve(n):
    if n <= 2 or n % 2 != 0:
        return []
        
    primes = get_primes(n)
    result = []
    
    i = 0
    while i < len(primes) and primes[i] <= n//2:
        p1 = primes[i]
        p2 = n - p1
        if p2 in primes[i:]:
            result.append(f"{p1}+{p2}")
        i += 1
            
    return result
```