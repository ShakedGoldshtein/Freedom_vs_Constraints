```python
def construct_graph_with_k_triangles(k: int) -> tuple[int, list[str]]:
    """
    Constructs an undirected graph with exactly k cycles of length 3 (triangles).
    The graph has at most 100 vertices.

    Args:
        k: The number of triangles required in the graph (1 <= k <= 1e5).

    Returns:
        A tuple (n, adjacency_matrix) where:
        - n is the number of vertices (3 <= n <= 100).
        - adjacency_matrix is a list of n strings of length n, representing the adjacency matrix.
    """
    if k == 0:
        return 3, ["000", "000", "000"]

    # Determine the minimal number of vertices needed
    n = _calculate_min_vertices(k)

    # Construct the graph
    if n == 3:
        return 3, ["011", "101", "110"]
    elif n == 4:
        return 4, ["0111", "1011", "1101", "1110"]
    else:
        return _construct_large_graph(k, n)

def _calculate_min_vertices(k: int) -> int:
    """
    Calculates the minimal number of vertices needed to form exactly k triangles.
    The solution uses the maximum number of triangles possible with n vertices,
    which is C(n, 3) for a complete graph, but we optimize for smaller n.
    """
    if k <= 1:
        return 3
    if k <= 4:
        return 4

    # For k >= 5, we use a complete graph on n vertices where C(n, 3) >= k.
    # We find the smallest n such that C(n, 3) >= k and n <= 100.
    n = 5
    while n <= 100:
        max_triangles = n * (n - 1) * (n - 2) // 6
        if max_triangles >= k:
            return n
        n += 1
    return 100  # Fallback, though problem guarantees k <= C(100, 3)

def _construct_large_graph(k: int, n: int) -> tuple[int, list[str]]:
    """
    Constructs a graph with exactly k triangles using n vertices.
    The graph is a complete graph minus some edges to reduce the number of triangles.
    """
    # Initialize a complete graph (all edges present except self-loops)
    adj = [['0'] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                adj[i][j] = '1'

    # Calculate the number of triangles in a complete graph
    total_triangles = n * (n - 1) * (n - 2) // 6
    if total_triangles == k:
        return n, [''.join(row) for row in adj]

    # Remove edges to reduce the number of triangles to exactly k
    # We remove edges from the last vertex to others to minimize the impact
    edges_to_remove = total_triangles - k
    if edges_to_remove <= 0:
        return n, [''.join(row) for row in adj]

    # Remove edges from vertex n-1 to others (excluding itself)
    # Each edge removal reduces the number of triangles by (n-2)
    # So we remove edges_to_remove // (n-2) edges, and handle the remainder
    edges_per_triangle = n - 2
    num_edges_to_remove = edges_to_remove // edges_per_triangle
    remaining_triangles = edges_to_remove % edges_per_triangle

    # Remove num_edges_to_remove edges from vertex n-1
    for i in range(n - 2, n - 2 - num_edges_to_remove, -1):
        if i >= 0:
            adj[n-1][i] = '0'
            adj[i][n-1] = '0'

    # If there's a remainder, remove one more edge and adjust
    if remaining_triangles > 0:
        if n - 2 - num_edges_to_remove - 1 >= 0:
            adj[n-1][n-2-num_edges_to_remove-1] = '0'
            adj[n-2-num_edges_to_remove-1][n-1] = '0'

    return n, [''.join(row) for row in adj]
```