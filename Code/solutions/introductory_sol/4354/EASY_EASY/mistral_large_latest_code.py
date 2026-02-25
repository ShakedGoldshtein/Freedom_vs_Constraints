```python
def padovan(n):
    if n < 0:
        return 0
    a, b, c = 1, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b
    return c
```