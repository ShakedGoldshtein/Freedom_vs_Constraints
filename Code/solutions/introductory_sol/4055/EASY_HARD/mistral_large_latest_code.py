```python
def solve(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '01'

    a, b = '0', '01'
    for _ in range(2, n + 1):
        a, b = b, b + a
    return b
```