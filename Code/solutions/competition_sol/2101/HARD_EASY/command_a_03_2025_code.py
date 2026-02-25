```python
def solve(n: int, m: int, edges: list[tuple[int, int]]) -> int:
    """
    Calculate the weight of the minimum spanning tree in a complete undirected weighted graph.

    Args:
        n (int): Number of vertices in the graph.
        m (int): Number of edges with weight 1.
        edges (list of tuples): List of edges with weight 1, where each tuple contains two vertices.

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
        if u_root != v_root:
            parent[v_root] = u_root
            return True
        return False

    # Sort edges to prioritize merging smaller components first
    edges.sort(key=lambda x: (min(find(x[0]), find(x[1])), max(find(x[0]), find(x[1]))))

    # Count the number of edges with weight 1 needed in the MST
    count = 0
    for u, v in edges:
        if union(u, v):
            count += 1
            if count == n - 1:
                break

    # The weight of the MST is the number of edges with weight 1
    return count
```