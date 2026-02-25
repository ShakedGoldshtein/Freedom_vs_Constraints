```python
def solve(n, k):
    if k == 1:
        return list(range(1, n+1))
        
    if k == n-1:
        # Alternating pattern
        result = list(range(1, n+1))
        for i in range(1, n-1, 2):
            result[i], result[i+1] = result[i+1], result[i]
        return result
        
    # General case
    result = [1] # Start with 1
    next_num = n
    used = set([1])
    
    # Add n as second number to get large diff
    result.append(next_num)
    used.add(next_num)
    next_num -= 1
    
    # Add remaining numbers with alternating diffs
    curr_diff = 1
    while len(result) < n:
        # Find next number that gives desired diff
        target = result[-1] + (-curr_diff if len(result) % 2 else curr_diff)
        
        if target > 0 and target <= n and target not in used:
            result.append(target)
            used.add(target)
        else:
            # Use next available number if target not possible
            while next_num in used:
                next_num -= 1
            result.append(next_num)
            used.add(next_num)
            next_num -= 1
            
        if len(set(abs(result[i] - result[i+1]) for i in range(len(result)-1))) > k:
            curr_diff += 1
            
    return result
```