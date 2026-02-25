```python
def digit_sum(n):
    """Calculate the sum of digits of a number."""
    return sum(int(i) for i in str(n))

def min_max_sum(l, d, x):
    """Find the minimum and maximum integer with sum of digits equal to x between l and d."""
    n = next(i for i in range(l, d + 1) if digit_sum(i) == x)
    m = next(i for i in range(d, l - 1, -1) if digit_sum(i) == x)
    return [n, m]
```