```python
def find_leaves(adj_list, n):
    leaves = []
    for v in range(1, n + 1):
        if len(adj_list[v]) == 1:
            leaves.append(v)
    return leaves

def get_path(adj_list, start, end, parent):
    path = []
    curr = end
    while curr != start:
        path.append(curr)
        curr = parent[curr]
    path.append(start)
    return path[::-1]

def get_all_paths(adj_list, leaves):
    paths = []
    for i in range(len(leaves)):
        for j in range(i+1, len(leaves)):
            visited = set()
            queue = [(leaves[i], [leaves[i]])]
            parent = {}
            
            while queue:
                vertex, path = queue.pop(0)
                if vertex == leaves[j]:
                    paths.append(get_path(adj_list, leaves[i], leaves[j], parent))
                    break
                
                for neighbor in adj_list[vertex]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        parent[neighbor] = vertex
                        queue.append((neighbor, path + [neighbor]))
    return paths

def get_edges_in_paths(paths, edges):
    edge_paths = []
    for path in paths:
        edge_path = []
        for i in range(len(path)-1):
            u, v = path[i], path[i+1]
            edge_idx = edges.index((min(u,v), max(u,v)))
            edge_path.append(edge_idx)
        edge_paths.append(edge_path)
    return edge_paths

def solve(n, edges):
    adj_list = [[] for _ in range(n+1)]
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    leaves = find_leaves(adj_list, n)
    
    if len(leaves) <= 2:
        return 1, 1
        
    paths = get_all_paths(adj_list, leaves)
    edge_paths = get_edges_in_paths(paths, edges)
    
    # For minimum value of f
    min_f = 1
    min_edges_covered = set()
    for path in edge_paths:
        for edge in path:
            min_edges_covered.add(edge)
    min_f = max(1, len(min_edges_covered)//2 + len(min_edges_covered)%2)
    
    # For maximum value of f
    max_f = len(edges)
    max_edges_covered = set()
    for edge in range(len(edges)):
        count = 0
        for path in edge_paths:
            if edge in path:
                count += 1
        if count > 0:
            max_edges_covered.add(edge)
            
    max_f = len(max_edges_covered)
    
    return min_f, max_f
```