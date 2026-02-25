```python
def digit_sum(n: int) -> int:
    """Calculate the sum of digits of a non-negative integer."""
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

def find_minimal_n(l: int, d: int, x: int) -> int:
    """Find the smallest n in [l, d] where digit_sum(n) == x."""
    for n in range(l, d + 1):
        if digit_sum(n) == x:
            return n
    return -1  # Should never happen per problem guarantees

def find_maximal_m(l: int, d: int, x: int) -> int:
    """Find the largest m in [l, d] where digit_sum(m) == x."""
    for m in range(d, l - 1, -1):
        if digit_sum(m) == x:
            return m
    return -1  # Should never happen per problem guarantees

def solve(l: int, d: int, x: int) -> list[int]:
    """Return [minimal_n, maximal_m] where digit sums equal x in [l, d]."""
    n = find_minimal_n(l, d, x)
    m = find_maximal_m(l, d, x)
    return [n, m]
```