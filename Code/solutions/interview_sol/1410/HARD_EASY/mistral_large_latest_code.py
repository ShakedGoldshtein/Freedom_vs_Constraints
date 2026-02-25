```python
import math
from functools import lru_cache

def solve(S, N, M, K):
    if K == 0:
        return 1.0
    if N < K or M - 1 < K:
        return 0.0
    if N >= M - 1:
        return 1.0

    total_ways = math.comb(S - 1, N - 1)
    if total_ways == 0:
        return 0.0

    favorable = 0.0
    for k in range(K, min(M - 1, N) + 1):
        ways = math.comb(M - 1, k) * math.comb(S - M, N - 1 - k)
        favorable += ways

    return favorable / total_ways

def solve_all(test_cases):
    results = []
    for case in test_cases:
        S, N, M, K = case
        prob = solve(S, N, M, K)
        results.append(prob)
    return results
```