```python
def solve(N, A, B, towns):
    total_fatigue = 0
    for i in range(1, N):
        walk_cost = (towns[i] - towns[i-1]) * A
        if walk_cost < B:
            total_fatigue += walk_cost
        else:
            total_fatigue += B
    return total_fatigue
```