```python
def solve_graph_shortest_paths_sum(n: int, adjacency_matrix: list[list[int]], deletion_order: list[int]) -> list[int]:
    """
    Calculates the sum of shortest path lengths between all pairs of remaining vertices
    before each vertex deletion step in a weighted directed graph.

    This function uses a reverse Floyd-Warshall approach. It conceptualizes adding vertices
    back to the graph in the reverse order of their deletion. At each "addition" step,
    the all-pairs shortest paths for the currently active set of vertices are updated,
    and the sum of these paths is recorded.

    The time complexity is O(N^3), where N is the number of vertices.
    The space complexity is O(N^2) for storing the distance matrix.

    Args:
        n: The number of vertices in the graph.
        adjacency_matrix: A list of lists representing the graph's adjacency matrix.
                          `adjacency_matrix[i][j]` is the weight of the edge from
                          vertex `i` to vertex `j`. Vertices are 0-indexed in this matrix.
        deletion_order: A list of `n` distinct integers representing the 1-indexed
                        vertices to be deleted, in order.

    Returns:
        A list of `n` integers, where the `i`-th number equals the required sum
        before the `i`-th deletion step (i.e., before deleting the `i`-th vertex
        in the `deletion_order` list). The results are returned in the same order
        as the deletion steps.
    """

    # Initialize shortest path distances matrix.
    # dist[i][j] will store the shortest path from vertex i to vertex j.
    # It's initialized with the direct edge weights from the adjacency matrix.
    # Vertices are 0-indexed internally (0 to n-1).
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = adjacency_matrix[i][j]

    # Convert 1-indexed deletion order to 0-indexed for internal use
    # and reverse the list to get the order in which vertices are "added back".
    # Example: if deletion_order = [x1, x2, ..., xn],
    # then reversed_addition_indices will process xn, then x(n-1), ..., then x1.
    reversed_addition_indices = [v - 1 for v in reversed(deletion_order)]

    # This list will store the sum of shortest paths at each step,
    # initially in reverse order of the problem's request.
    results_in_reverse_order = []
    
    # A set to keep track of vertices that are currently "active" in the graph.
    # These are the vertices that have been conceptually re-added.
    active_vertices = set()

    # Iterate through vertices in the reverse deletion order (effectively, addition order).
    # `k_val_idx` is the 0-indexed vertex that is currently being "added back" to the graph.
    for k_val_idx in reversed_addition_indices:
        # Add the current vertex to the set of active vertices.
        active_vertices.add(k_val_idx)

        # Apply the Floyd-Warshall update step for the newly active vertex `k_val_idx`.
        # This updates the shortest paths `dist[i][j]` for all pairs `(i, j)` in the
        # original `N`-vertex graph. It considers `k_val_idx` as a potential
        # intermediate vertex, in addition to any previously activated vertices.
        # This ensures that `dist[i][j]` always holds the shortest path between `i` and `j`
        # using only intermediate vertices from the set of currently `active_vertices`.
        for i in range(n):
            for j in range(n):
                # Update path from i to j through k_val_idx
                dist[i][j] = min(dist[i][j], dist[i][k_val_idx] + dist[k_val_idx][j])

        # Calculate the sum of shortest paths for all distinct pairs of
        # vertices that are currently in the `active_vertices` set.
        current_step_sum = 0
        for u in active_vertices:
            for v in active_vertices:
                if u != v:  # Sum for v != u as per problem statement
                    current_step_sum += dist[u][v]
        
        # Store the calculated sum. Since we are iterating in reverse deletion order,
        # the sums are collected in reverse of the desired output order.
        results_in_reverse_order.append(current_step_sum)
    
    # Reverse the collected results to match the problem's output requirement:
    # the i-th number equals the required sum before the i-th step.
    return list(reversed(results_in_reverse_order))
```