```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(n, p):
    count = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if gcd(i * j, p) == 1:
                count += 1
    return count

def solve_multiple(test_cases):
    results = []
    for n, p in test_cases:
        results.append(solve(n, p))
    return results
```