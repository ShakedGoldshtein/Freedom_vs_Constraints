```python
def min_spanning_tree_weight(n, m, edges):
    if m == 0:
        return 0
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return False
        if rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[u_root] = v_root
            if rank[u_root] == rank[v_root]:
                rank[v_root] += 1
        return True

    edges.sort(key=lambda x: (x[2], x[0], x[1]))
    mst_edges = 0
    total_weight = 0

    for a, b in edges:
        if union(a, b):
            total_weight += 1
            mst_edges += 1
            if mst_edges == n - 1:
                break

    return total_weight
```