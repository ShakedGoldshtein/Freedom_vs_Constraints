```python
def solve(n):
    if n == 0: return '0'
    if n == 1: return '01'
    
    f0 = '0'
    f1 = '01'
    
    for i in range(2, n+1):
        f1, f0 = f1 + f0, f1
        
    return f1
```