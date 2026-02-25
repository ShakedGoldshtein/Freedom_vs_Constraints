```python
def solve(n, k):
    """
    Find permutation p of length n where absolute differences between adjacent elements have k distinct values
    Returns list of n integers forming valid permutation
    """
    # Special case when k=1 - return sorted sequence
    if k == 1:
        return list(range(1, n+1))
        
    # For k=2, create alternating sequence like 1,3,2,4,5...
    if k == 2:
        result = list(range(1, n+1))
        for i in range(1, min(n-1, 3), 2):
            result[i], result[i+1] = result[i+1], result[i]
        return result
        
    # For larger k, create sequence with differences 1,2,...,k-1,1,1,...
    result = [0] * n
    result[0] = 1
    
    # Fill first k positions to get k-1 distinct differences
    curr = 1
    for i in range(1, k):
        curr += i
        result[i] = curr
        
    # Fill remaining positions
    curr = 2
    for i in range(k, n):
        result[i] = curr
        curr += 1
        
    # Validate and fix if needed to get valid permutation
    used = set(result)
    unused = set(range(1, n+1)) - used
    
    for i in range(n):
        if result[i] > n:
            result[i] = unused.pop()
            
    return result
```