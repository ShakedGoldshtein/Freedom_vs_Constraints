```python
def solve(N, A, B, X):
    total = 0
    for i in range(1, N):
        walk_cost = (X[i] - X[i-1]) * A
        total += min(walk_cost, B)
    return total
```