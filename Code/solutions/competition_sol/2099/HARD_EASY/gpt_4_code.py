```python
def solve(n, k):
    p = [0] * n
    p[::2] = range(1, k + 2)
    p[1::2] = range(k + 2, n + 1)
    return p
```