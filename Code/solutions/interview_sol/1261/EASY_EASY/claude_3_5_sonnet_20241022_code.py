```python
def solve(testcases):
    result = []
    for n, m in testcases:
        # Check if impossible
        min_edges = n # Minimum edges needed for cycle
        max_edges = n * (n-1) // 2 # Maximum possible edges
        
        if m < min_edges or m > max_edges:
            result.append([(-1, -1)])
            continue
        
        # Construct cycle first to satisfy 2nd requirement
        edges = []
        for i in range(1, n):
            edges.append((i, i+1))
        edges.append((n, 1))
        
        # Add remaining edges
        edges_to_add = m - n
        if edges_to_add > 0:
            for i in range(1, n-1):
                for j in range(i+2, n+1):
                    if edges_to_add == 0:
                        break
                    edges.append((i,j))
                    edges_to_add -= 1
                if edges_to_add == 0:
                    break
                    
        result.append(edges)
        
    return result
```