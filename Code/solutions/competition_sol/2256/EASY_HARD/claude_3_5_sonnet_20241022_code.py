```python
def solve(n, m):
    if n == 1 and m == 1:
        return [(1,1)]
    
    if n == 1 and m == 2:
        return [(1,1), (1,2)]
        
    if n == 2 and m == 2:
        return [(1,1), (2,2), (1,2), (2,1)]
        
    if n == 1 or m == 1:
        if max(n,m) == 2:
            return [(1,1), (1,2)] if m > n else [(1,1), (2,1)]
        return -1
        
    # For 2xM and Nx2, use zigzag pattern
    if n == 2:
        result = [(1,1)]
        for i in range(2, m+1):
            if i % 2 == 0:
                result.append((2,i))
                if i < m:
                    result.append((1,i))
            else:
                result.append((2,i))
                if i < m:
                    result.append((1,i+1))
        result.append((1,2))
        for i in range(3,m,2):
            result.append((1,i))
        return result
        
    if m == 2:
        result = [(1,1)]
        for i in range(2, n+1):
            if i % 2 == 0:
                result.append((i,2))
                if i < n:
                    result.append((i,1))
            else:
                result.append((i,2))
                if i < n:
                    result.append((i+1,1))
        result.append((2,1))
        for i in range(3,n,2):
            result.append((i,1))
        return result
        
    # For general case NxM where N,M >= 3
    result = [(1,1)]
    
    # Fill first row
    for i in range(2, m+1):
        result.append((1,i))
    
    # Fill rest of rows in zigzag
    curr_row = 2
    while curr_row <= n:
        if curr_row % 2 == 0:
            for i in range(m,0,-1):
                result.append((curr_row,i))
        else:
            for i in range(1,m+1):
                result.append((curr_row,i))
        curr_row += 1
        
    return result
```