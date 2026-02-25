```python
def solve(n):
    res = []
    for i in range(1, n + 1):
        res.append(i * (i + 1) * (i + 1) - (i - 1))
    return res
```