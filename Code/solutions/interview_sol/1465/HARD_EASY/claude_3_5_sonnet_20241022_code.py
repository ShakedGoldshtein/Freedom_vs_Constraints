```python
def find_path(u, v, adj):
    def dfs(curr, target, path, visited):
        if curr == target:
            return path
        visited.add(curr)
        for nxt in adj[curr]:
            if nxt not in visited:
                path.append(nxt)
                result = dfs(nxt, target, path, visited)
                if result:
                    return result
                path.pop()
        return None

    path = [u]
    visited = set()
    return dfs(u, v, path, visited)

def get_edge_indices(path, edge_map):
    edge_indices = []
    for i in range(len(path)-1):
        u, v = path[i], path[i+1]
        if (u,v) in edge_map:
            edge_indices.append(edge_map[(u,v)])
        else:
            edge_indices.append(edge_map[(v,u)])
    return edge_indices

def count_valid_assignments(n, edges, conditions):
    MOD = 10**9 + 7
    
    # Build adjacency list
    adj = [[] for _ in range(n+1)]
    edge_map = {}
    for i, (u, v) in enumerate(edges):
        adj[u].append(v)
        adj[v].append(u)
        edge_map[(u,v)] = i
        edge_map[(v,u)] = i
        
    # Get paths for each condition
    paths = []
    for u, v, x in conditions:
        path = find_path(u, v, adj)
        paths.append((get_edge_indices(path, edge_map), x))
        
    # Try all possible edge weight assignments
    total = 0
    for mask in range(1 << len(edges)):
        valid = True
        for path_edges, x in paths:
            path_sum = sum((mask >> i) & 1 for i in path_edges)
            if path_sum % 2 != x:
                valid = False
                break
        if valid:
            total = (total + 1) % MOD
            
    return total

def solve(T, cases):
    result = []
    for _ in range(T):
        n, Q = cases[_][0]
        edges = cases[_][1]
        conditions = cases[_][2]
        result.append(count_valid_assignments(n, edges, conditions))
    return result
```