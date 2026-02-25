```python
def digit_sum(n):
    """Calculate sum of digits in number n."""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def find_min_num(l, d, x):
    """Find minimum number n between l and d with digit sum x."""
    for n in range(l, d+1):
        if digit_sum(n) == x:
            return n
    return None

def find_max_num(l, d, x):
    """Find maximum number m between l and d with digit sum x."""
    for m in range(d, l-1, -1):
        if digit_sum(m) == x:
            return m
    return None

def solve(l, d, x):
    """
    Find numbers with min/max digit sum between l and d equal to x.
    Returns array [min number, max number]
    """
    min_num = find_min_num(l, d, x)
    max_num = find_max_num(l, d, x)
    
    if min_num is not None and max_num is not None:
        return [min_num, max_num]
    
    return None
```