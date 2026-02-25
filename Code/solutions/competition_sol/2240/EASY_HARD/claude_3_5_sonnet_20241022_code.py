```python
def solve(n, edges, values):
    adj = [[] for _ in range(n+1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
        
    # Find vertices reachable from vertex 1
    def get_subtree(parent, vertex, subtree):
        subtree.append(vertex)
        for next_v in adj[vertex]:
            if next_v != parent:
                get_subtree(vertex, next_v, subtree)
    
    # Get full tree starting from vertex 1        
    subtree = []
    get_subtree(0, 1, subtree)
    
    # Find values at indices in subtree
    vals = [values[i-1] for i in subtree]
    
    # Check if all values can be made 0
    if len(set(vals)) == 1:
        return abs(vals[0])
        
    # Values need to be equalized first, then zeroed
    maximum = max(vals)
    minimum = min(vals)
    
    # Count steps needed:
    # 1) Steps to bring min up to 0 or max down to 0
    # 2) Steps from there to reach 0 for all
    if abs(maximum) > abs(minimum):
        return abs(maximum - minimum) + abs(minimum)
    return abs(maximum - minimum) + abs(maximum)
```