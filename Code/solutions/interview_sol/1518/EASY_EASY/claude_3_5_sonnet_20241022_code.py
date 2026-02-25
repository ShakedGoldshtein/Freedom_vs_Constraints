```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(n, k):
    if k == 1:
        return 1 if is_prime(n) else 0
        
    if k == 2:
        for i in range(2, n//2 + 1):
            if is_prime(i) and is_prime(n-i):
                return 1
        return 0
        
    if k >= 3:
        if n < 2*k:
            return 0
        if n % 2 == 0 or n >= 2*k + 1:
            return 1
        return 0

def solve_all(test_cases):
    results = []
    for n, k in test_cases:
        results.append(solve(n, k))
    return results
```