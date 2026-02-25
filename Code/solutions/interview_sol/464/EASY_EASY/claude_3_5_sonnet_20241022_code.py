```python
def solve(n):
    arr = [(2 * i) + 1 for i in range(n)]
    target = sum(arr) // n
    ops = 0
    
    for num in arr:
        ops += abs(num - target)
    
    return ops // 2
```