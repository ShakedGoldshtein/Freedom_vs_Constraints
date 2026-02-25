```python
import math
from functools import lru_cache

@lru_cache(maxsize=None)
def comb(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return comb(n-1, k-1) + comb(n-1, k)

def solve(S, N, M, K):
    if N < K + 1:
        return 0.0
    if N >= M:
        return 1.0
    total_ways = comb(S - 1, N - 1)
    valid_ways = 0
    for k in range(K, min(M, N)):
        ways = comb(M - 1, k) * comb(S - M, N - 1 - k)
        valid_ways += ways
    return valid_ways / total_ways
```