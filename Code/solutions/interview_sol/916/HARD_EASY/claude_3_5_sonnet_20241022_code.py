```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve_single_case(n, m):
    # Minimum amount each person can pay with their coins should be equal
    # This means we need to find the least common multiple of N and M
    return (n * m) // gcd(n, m)

def solve(test_cases):
    result = []
    for n, m in test_cases:
        result.append(solve_single_case(n, m))
    return result
```