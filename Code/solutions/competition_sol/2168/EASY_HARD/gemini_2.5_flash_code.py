```python
def solve(n: int, adj_matrix: list[list[int]], deletion_order_input: list[int]) -> list[int]:
    """
    Calculates the sum of shortest path lengths between all pairs of remaining vertices
    before each vertex removal in a weighed directed graph.

    Args:
        n: The number of vertices in the graph.
        adj_matrix: The n x n adjacency matrix representing edge weights.
                    a_ij is the weight of the edge from i to j. a_ii = 0.
        deletion_order_input: A list of n distinct integers (1-indexed) representing
                              the order in which vertices are deleted.

    Returns:
        A list of n integers, where the i-th number is the required sum
        before the i-th step (i.e., before deleting x_i).
    """

    # Convert 1-indexed input vertices to 0-indexed for easier list/array access
    deletion_order = [x - 1 for x in deletion_order_input]

    # Initialize the distance matrix with the given adjacency matrix.
    # We use a deep copy to avoid modifying the original input adjacency matrix.
    dist = [row[:] for row in adj_matrix]

    # Store the results for each step.
    # Results will be collected in reverse order of deletion, then reversed again at the end.
    results = []

    # The problem asks for the sum before each vertex removal.
    # This is equivalent to calculating the sum for graphs with (n), (n-1), ..., (1) vertices.
    # We can solve this efficiently by reversing the deletion order and adding vertices
    # one by one, using a modified Floyd-Warshall algorithm.
    # `insertion_order` represents the vertices being added back into the graph.
    insertion_order = deletion_order[::-1]

    # `active_vertices` keeps track of the vertices currently present in the graph.
    active_vertices = set()

    # Iterate through vertices in reverse deletion order (i.e., insertion order).
    # `k_added` is the vertex currently being "activated" or added to the graph.
    for k_added in insertion_order:
        # Add the current vertex to the set of active vertices.
        active_vertices.add(k_added)

        # Now that `k_added` is active, it can be used as an intermediate vertex.
        # We perform updates similar to the Floyd-Warshall algorithm.
        # The key is to ensure that paths *to* and *from* `k_added` are minimized
        # using other active vertices as intermediates, before `k_added` itself
        # is used as an intermediate for other pairs.

        # Step 1: Update paths involving `k_added` as an endpoint.
        # For any pair of currently active vertices (i, j), check if going via `j`
        # shortens the path from `i` to `k_added`, or from `k_added` to `j`.
        # This ensures that `dist[i][k_added]` and `dist[k_added][j]` are minimized
        # considering all active intermediate vertices *before* `k_added` itself is used as the pivot.
        for i in active_vertices:
            for j in active_vertices:
                if dist[i][j] + dist[j][k_added] < dist[i][k_added]:
                    dist[i][k_added] = dist[i][j] + dist[j][k_added]
                if dist[k_added][i] + dist[i][j] < dist[k_added][j]:
                    dist[k_added][j] = dist[k_added][i] + dist[i][j]

        # Step 2: Update all-pairs shortest paths among active vertices using `k_added` as an intermediate.
        # After Step 1, `dist[i][k_added]` and `dist[k_added][j]` are up-to-date for all `i, j` in `active_vertices`.
        # Now, we use `k_added` as the central pivot to potentially shorten paths between any other `i, j`.
        for i in active_vertices:
            for j in active_vertices:
                if dist[i][k_added] + dist[k_added][j] < dist[i][j]:
                    dist[i][j] = dist[i][k_added] + dist[k_added][j]

        # Calculate the sum of shortest paths between all pairs of *currently* active vertices.
        current_total_sum = 0
        for u in active_vertices:
            for v in active_vertices:
                if u != v:  # Exclude paths from a vertex to itself as per problem sum definition
                    current_total_sum += dist[u][v]
        
        # Add the sum to results. This sum corresponds to the graph state
        # *before* the removal of the vertex that is next in `deletion_order`.
        results.append(current_total_sum)

    # The results were collected in the reverse order of deletion.
    # Reverse the `results` list to match the requested output order (before deleting x_1, then x_2, etc.).
    return results[::-1]
```