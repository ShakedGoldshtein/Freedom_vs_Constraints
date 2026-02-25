```python
def solve(n, arr):
    # Impossible cases
    if n == 1:
        return [-1]
    
    # For n=2 just swap
    if n == 2:
        return [arr[1], arr[0]]
        
    # For n>=3, sort ascending and then rotate right by 1
    arr.sort()
    b = [arr[-1]] + arr[:-1]
    
    return b
```