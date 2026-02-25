```python
import math

def solve(T, test_cases):
    results = []
    for N, M in test_cases:
        lcm = (N * M) // math.gcd(N, M)
        results.append(lcm)
    return results
```