```python
def minimum_spanning_tree_weight(n, m, edges):
    """
    Computes the weight of the minimum spanning tree (MST) for a complete graph where edges
    are either 0 or 1, with exactly m edges having weight 1. The MST weight is the sum of
    the weights of the edges in the MST.

    Args:
        n (int): Number of vertices in the graph.
        m (int): Number of edges with weight 1.
        edges (list[tuple[int, int]]): List of edges with weight 1, each as a tuple (a, b).

    Returns:
        int: Weight of the MST.
    """
    if n == 1:
        return 0

    parent = list(range(n + 1))  # 1-based indexing
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

    # Kruskal's algorithm: process edges in order of increasing weight (0 first, then 1)
    # Since all edges are either 0 or 1, we can first connect all 0-weight edges (which are all possible edges not in 'edges')
    # Then, we connect the remaining components using the 1-weight edges.

    # Step 1: Connect all 0-weight edges (all edges not in 'edges' are 0-weight)
    # To simulate this, we can union all pairs not in 'edges', but that's O(n^2) which is too slow for n=1e5.
    # Instead, we can observe that the MST will use as many 0-weight edges as possible.
    # The MST will have (n-1) edges. The minimal weight is achieved by using as many 0-weight edges as possible.
    # The number of 0-weight edges in the MST is (n-1) minus the number of 1-weight edges needed to connect all components formed by 0-weight edges.

    # The components formed by 0-weight edges are the connected components in the complement graph of the 1-weight edges.
    # So, we first find the connected components of the graph where edges are the 1-weight edges.
    # Then, the number of 0-weight edges in the MST is (n - k), where k is the number of connected components in the 1-weight graph.
    # The number of 1-weight edges in the MST is (k - 1), because we need (k-1) edges to connect k components.
    # Thus, the total weight is (k - 1) * 1 + (n - k) * 0 = (k - 1).

    # So, the problem reduces to finding the number of connected components in the graph formed by the 1-weight edges.
    # The MST weight is then (number of connected components - 1).

    # Initialize DSU for the 1-weight edges
    for a, b in edges:
        union(a, b)

    # Count the number of connected components
    components = set()
    for u in range(1, n + 1):
        components.add(find(u))

    return len(components) - 1
```