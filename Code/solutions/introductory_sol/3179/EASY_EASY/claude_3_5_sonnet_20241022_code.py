```python
def solve(l, d, x):
    def digit_sum(n):
        return sum(int(d) for d in str(n))
    
    # Find minimal n
    n = l
    while n <= d:
        if digit_sum(n) == x:
            break
        n += 1
            
    # Find maximal m    
    m = d
    while m >= l:
        if digit_sum(m) == x:
            break
        m -= 1
        
    return [n, m]
```