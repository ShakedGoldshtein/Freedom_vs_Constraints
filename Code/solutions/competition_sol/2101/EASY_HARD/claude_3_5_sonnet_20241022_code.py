```python
def solve(n, m, edges=None):
    if m == 0:
        return 0
        
    if edges is None:
        return 0
        
    # Create adjacency matrix
    adj = [[0]*n for _ in range(n)]
    for a,b in edges:
        adj[a-1][b-1] = 1
        adj[b-1][a-1] = 1
    
    # Prim's algorithm
    selected = [False] * n
    selected[0] = True
    edge_count = 0
    min_weight = 0
    
    while edge_count < n - 1:
        minimum = float('inf')
        x = 0
        y = 0
        
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and adj[i][j] != float('inf'):
                        if minimum > adj[i][j]:
                            minimum = adj[i][j]
                            x = i
                            y = j
        
        selected[y] = True
        min_weight += minimum
        edge_count += 1
    
    return min_weight
```