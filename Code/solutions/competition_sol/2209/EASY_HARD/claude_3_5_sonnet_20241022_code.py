```python
def find_leaves(n, edges):
    adj = [[] for _ in range(n+1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    leaves = []
    for i in range(1, n+1):
        if len(adj[i]) == 1:
            leaves.append(i)
    return leaves

def find_paths(adj, u, p, paths, curr_path):
    if len(adj[u]) == 1 and adj[u][0] == p:
        paths.append(curr_path[:])
        return
    
    for v in adj[u]:
        if v != p:
            curr_path.append([u,v])
            find_paths(adj, v, u, paths, curr_path)
            curr_path.pop()

def solve(n, edges):
    adj = [[] for _ in range(n+1)]
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    leaves = find_leaves(n, edges)
    
    # For maximum value
    if len(leaves) == 2:
        return 1, len(edges)
        
    paths = []
    find_paths(adj, leaves[0], -1, paths, [])
    
    # For minimum value
    min_f = 1
    if any(len(p) % 2 == 1 for p in paths):
        min_f = 3
        
    # For maximum value    
    max_f = len(edges)
    if len(paths) >= 2:
        # Check if paths share edges
        edge_set = set()
        for p in paths:
            for e in p:
                e = tuple(sorted(e))
                edge_set.add(e)
        max_f = len(edge_set)
        
    if max_f < min_f:
        max_f = min_f
        
    return min_f, max_f
```