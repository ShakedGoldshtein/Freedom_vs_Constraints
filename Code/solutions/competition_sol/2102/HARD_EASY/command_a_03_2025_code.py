```python
def generate_graph(k: int) -> tuple[int, list[str]]:
    """
    Generates a graph with exactly k cycles of length 3.

    Args:
        k (int): The number of cycles of length 3 required in the graph.

    Returns:
        tuple: A tuple containing:
            - n (int): The number of vertices in the graph.
            - adjacency_matrix (list of str): The adjacency matrix of the graph as a list of strings.
    """
    # Calculate the number of vertices needed to achieve exactly k cycles of length 3.
    # The formula is derived from the fact that in a complete graph with n vertices,
    # the number of triangles (cycles of length 3) is given by C(n, 3) = n*(n-1)*(n-2)/6.
    # We need to find the smallest n such that C(n, 3) >= k.
    n = 3
    while n * (n - 1) * (n - 2) // 6 < k:
        n += 1

    # Initialize the adjacency matrix with all zeros.
    adjacency_matrix = [[0] * n for _ in range(n)]

    # Fill the adjacency matrix to create a complete graph with n vertices.
    # A complete graph ensures that every pair of distinct vertices is connected by a unique edge.
    for i in range(n):
        for j in range(n):
            if i != j:
                adjacency_matrix[i][j] = 1

    # If the number of cycles in the complete graph is greater than k,
    # remove edges to reduce the number of cycles to exactly k.
    total_cycles = n * (n - 1) * (n - 2) // 6
    if total_cycles > k:
        # Calculate the number of edges to remove to reduce the number of cycles.
        edges_to_remove = total_cycles - k
        # Iterate through the upper triangle of the adjacency matrix to remove edges.
        for i in range(n):
            for j in range(i + 1, n):
                if edges_to_remove == 0:
                    break
                # Remove the edge between vertices i and j.
                adjacency_matrix[i][j] = 0
                adjacency_matrix[j][i] = 0
                edges_to_remove -= 1

    # Convert the adjacency matrix to a list of strings for output.
    adjacency_matrix_str = ["".join(map(str, row)) for row in adjacency_matrix]

    return n, adjacency_matrix_str


def solve(k: int) -> tuple[int, list[str]]:
    """
    Solves the problem of generating a graph with exactly k cycles of length 3.

    Args:
        k (int): The number of cycles of length 3 required in the graph.

    Returns:
        tuple: A tuple containing:
            - n (int): The number of vertices in the graph.
            - adjacency_matrix (list of str): The adjacency matrix of the graph as a list of strings.
    """
    return generate_graph(k)
```