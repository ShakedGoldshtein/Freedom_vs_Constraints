```python
from math import comb

def solve(S, N, M, K):
    if N - 1 < K:
        return 0.0
    if S - M < N - 1:
        return 1.0
    
    total_ways = comb(S - 1, N - 1)
    favorable = 0
    for i in range(K, min(M, N)):
        favorable += comb(M - 1, i) * comb(S - M, N - 1 - i)
    
    return favorable / total_ways

t = int(input().strip())
for _ in range(t):
    S, N, M, K = map(int, input().split())
    result = solve(S, N, M, K)
    print(f"{result:.6f}")
```