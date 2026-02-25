```python
def solve(n, q, arr, queries):
    if n == 0:
        return []
    
    max_val = max(arr)
    max_index = arr.index(max_val)
    
    cycles = []
    current = arr[:]
    
    for i in range(n):
        A = current[0]
        B = current[1]
        cycles.append((A, B))
        
        if A > B:
            current = [A] + current[2:] + [B]
        else:
            current = [B] + current[2:] + [A]
        
        if current[0] == max_val:
            break
    
    fixed_ops = len(cycles)
    remaining = current[1:]
    
    result = []
    for m in queries:
        if m <= fixed_ops:
            A, B = cycles[m - 1]
            result.append((A, B))
        else:
            index = (m - fixed_ops - 1) % (n - 1)
            A = max_val
            B = remaining[index]
            result.append((A, B))
    
    return result
```