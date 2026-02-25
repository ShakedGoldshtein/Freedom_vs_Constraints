```python
def solve(T, cases):
    def valid_network(n, m):
        # For first requirement, we need at least n-1 edges
        if m < n-1:
            return None
            
        # For second requirement, we need at least n edges
        # to ensure network remains connected after any node failure
        if m < n:
            return None
            
        # Check if too many edges requested
        max_edges = n * (n-1) // 2
        if m > max_edges:
            return None
            
        # For n <= 2, cannot satisfy requirements
        if n <= 2:
            return None
            
        # For valid case, construct edges in circular fashion
        # plus additional edges as needed
        edges = []
        
        # First create circular connection
        for i in range(n-1):
            edges.append((i+1, i+2))
        edges.append((n, 1))
        
        # Add remaining edges diagonally
        if m > n:
            curr = 1
            skip = 2
            while len(edges) < m and skip < n:
                for i in range(1, n+1-skip):
                    if len(edges) >= m:
                        break
                    edges.append((i, i+skip))
                skip += 1
                
        return edges
    
    result = []
    for n, m in cases:
        network = valid_network(n, m)
        if network is None:
            result.append([(-1, -1)])
        else:
            result.append(network)
            
    return result
```