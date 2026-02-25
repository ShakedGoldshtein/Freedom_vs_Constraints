```python
def padovan(n):
    if n < 0:
        return 0
    if n <= 2:
        return 1
        
    p0, p1, p2 = 1, 1, 1
    for i in range(3, n + 1):
        curr = p0 + p1
        p0 = p1
        p1 = p2
        p2 = curr
        
    return p2
```