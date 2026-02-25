```python
def solve(n):
    results = []
    current = 2
    for k in range(1, n + 1):
        target_sqrt = k + 1
        target_square = target_sqrt * target_sqrt
        presses = (target_square * k - current) // k
        results.append(presses)
        current = target_sqrt
    return results
```