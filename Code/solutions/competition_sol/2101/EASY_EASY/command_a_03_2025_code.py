```python
def solve(n: int, m: int, edges: list[tuple[int, int]]) -> int:
    """
    Calculate the weight of the minimum spanning tree of a complete graph with edges of weight 0 or 1.

    Args:
        n (int): The number of vertices in the graph.
        m (int): The number of edges with weight 1.
        edges (list of tuples): List of edges where each edge is represented as a tuple (a, b).

    Returns:
        int: The weight of the minimum spanning tree.
    """
    if n == 1:
        return 0

    # Initialize the parent array for Union-Find
    parent = list(range(n + 1))

    def find(u: int) -> int:
        """
        Find the root of the set containing u with path compression.

        Args:
            u (int): The vertex to find the root for.

        Returns:
            int: The root of the set containing u.
        """
        while parent[u] != u:
            parent[u] = parent[parent[u]]  # Path compression
            u = parent[u]
        return u

    def union(u: int, v: int) -> bool:
        """
        Union the sets containing u and v.

        Args:
            u (int): The first vertex.
            v (int): The second vertex.

        Returns:
            bool: True if the sets were merged, False if they were already in the same set.
        """
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return False
        parent[v_root] = u_root
        return True

    # Sort edges to prioritize merging vertices with the most connections
    # This ensures that we merge vertices with the highest degree first, reducing the number of edges with weight 1
    edges.sort(key=lambda x: -min(x))

    # Initialize the result (weight of the minimum spanning tree)
    result = 0

    # Iterate through the sorted edges and union the vertices
    for u, v in edges:
        if union(u, v):
            result += 1
            if find(1) == find(n):
                break

    # If not all vertices are connected, we need to add edges of weight 0
    # The number of additional edges needed is (n - 1) - result
    if find(1) != find(n):
        result += (n - 1) - result

    return result
```