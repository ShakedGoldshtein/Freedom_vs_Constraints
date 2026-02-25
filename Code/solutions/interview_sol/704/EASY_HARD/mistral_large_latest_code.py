```python
def solve(A, N, M):
    if A == 0:
        return 0
    mod = 0
    power = 1
    for _ in range(N):
        mod = (mod * (10 ** len(str(A))) + A) % M
    return mod
```