```python
def find_set(parent, x):
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x])
    return parent[x]

def union_sets(parent, rank, x, y):
    px, py = find_set(parent, x), find_set(parent, y)
    if px == py:
        return
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1

def solve(n, m, edges=None):
    if edges is None:
        edges = []
    
    # Initialize disjoint set data structures
    parent = list(range(n+1))
    rank = [0] * (n+1)
    
    # Add edges of weight 1 to set of weighted edges
    weight_one_edges = set()
    for a, b in edges:
        weight_one_edges.add(tuple(sorted([a,b])))
    
    # Run Kruskal's algorithm
    mst_weight = 0
    edges_used = 0
    
    # First try edges of weight 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if tuple([i,j]) not in weight_one_edges:
                if find_set(parent, i) != find_set(parent, j):
                    union_sets(parent, rank, i, j)
                    edges_used += 1
    
    # Then try edges of weight 1
    sorted_edges = [(1, a, b) for a, b in weight_one_edges]
    for w, u, v in sorted_edges:
        if edges_used == n-1:
            break
        if find_set(parent, u) != find_set(parent, v):
            union_sets(parent, rank, u, v)
            mst_weight += w
            edges_used += 1
            
    return mst_weight
```