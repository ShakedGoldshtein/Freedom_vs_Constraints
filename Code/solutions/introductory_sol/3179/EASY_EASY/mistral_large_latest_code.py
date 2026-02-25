```python
def digit_sum(n):
    return sum(int(d) for d in str(n))

def solve(l, d, x):
    n, m = None, None
    for num in range(l, d + 1):
        if digit_sum(num) == x:
            if n is None:
                n = num
            m = num
    return [n, m]
```