```python
def solve(n, arr):
    result = []
    used = [False] * n
    
    while True:
        current = []
        last = float('-inf')
        
        for i in range(n):
            if not used[i] and arr[i] > last:
                current.append(arr[i])
                last = arr[i]
                used[i] = True
                
        if not current:
            break
            
        result.append(current)
        
    return result
```