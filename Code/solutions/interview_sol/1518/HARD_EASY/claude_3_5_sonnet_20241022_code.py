```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes_up_to(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def can_sum_k_primes(n, k):
    if n < 2*k:
        return 0
        
    if k == 1:
        return 1 if is_prime(n) else 0
        
    if k == 2:
        primes = get_primes_up_to(n)
        for p in primes:
            if p > n//2:
                break
            if n-p in primes:
                return 1
        return 0
        
    # Goldbach conjecture for k >= 3
    if k >= 3 and n >= 2*k:
        return 1
    
    return 0

def solve(test_cases):
    results = []
    for n, k in test_cases:
        results.append(can_sum_k_primes(n, k))
    return results
```