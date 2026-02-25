```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_good_pairs(n, p):
    good_pairs = 0
    for a in range(1, n):
        for b in range(a + 1, n + 1):
            if gcd(a * b, p) == 1:
                good_pairs += 1
    return good_pairs

def solve(test_cases):
    results = []
    for _ in range(test_cases):
        n, p = test_cases[_]
        results.append(count_good_pairs(n, p))
    return results
```