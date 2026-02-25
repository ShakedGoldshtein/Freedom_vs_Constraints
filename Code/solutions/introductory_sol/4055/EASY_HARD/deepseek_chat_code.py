```python
def solve(n):
    if n == 0:
        return '0'
    if n == 1:
        return '01'
    
    prev_prev = '0'
    prev = '01'
    
    for i in range(2, n + 1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
    
    return prev
```