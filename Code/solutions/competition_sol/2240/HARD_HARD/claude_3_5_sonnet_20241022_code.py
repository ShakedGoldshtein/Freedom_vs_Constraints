```python
def solve(n, edges, values):
    # Build adjacency list representation
    adj = [[] for _ in range(n+1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
        
    # Find set of vertices reachable from vertex 1
    def get_reachable(start, parent):
        reachable = {start}
        for v in adj[start]:
            if v != parent:
                reachable.update(get_reachable(v, start))
        return reachable
        
    reachable = get_reachable(1, -1)
    
    # Convert vertex set to indices
    indices = {i-1 for i in reachable}
    
    # While any value is non-zero
    moves = 0
    while any(values[i] != 0 for i in range(n)):
        # Check if all reachable vertices have same sign
        pos = neg = 0
        for i in indices:
            if values[i] > 0:
                pos += 1
            elif values[i] < 0:
                neg += 1
                
        # If mixed signs, we can't make progress
        if pos > 0 and neg > 0:
            return -1
            
        # Find max absolute value in subtree
        max_abs = 0
        for i in indices:
            max_abs = max(max_abs, abs(values[i]))
            
        # If positive values, decrease by max
        # If negative values, increase by max
        change = max_abs if pos > 0 else -max_abs
        moves += abs(change)
        
        # Apply change to subtree
        for i in indices:
            values[i] -= change
            
    return moves
```