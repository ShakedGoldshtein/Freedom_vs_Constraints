```python
def solve(l, d, x):
    def digit_sum(num):
        return sum(int(digit) for digit in str(num))
    
    n = None
    m = None
    
    for i in range(l, d + 1):
        if digit_sum(i) == x:
            n = i
            break
    
    for i in range(d, l - 1, -1):
        if digit_sum(i) == x:
            m = i
            break
    
    return [n, m]
```