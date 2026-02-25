```python
def solve(k: int) -> list[str]:
    """
    Finds an undirected graph with exactly k cycles of length 3 (triangles).
    The number of vertices should not exceed 100.

    Args:
        k: The desired number of 3-cycles (1 <= k <= 10^5).

    Returns:
        A list of strings representing the adjacency matrix of the graph.
        The first element is the number of vertices n, followed by n strings
        each representing a row of the adjacency matrix.
    """

    # Initialize an adjacency matrix for up to 100 vertices, all disconnected
    adj = [[0 for _ in range(100)] for _ in range(100)]
    
    n_nodes = 0  # Tracks the current total number of nodes used in the graph
    current_triangles_count = 0 # Tracks the number of 3-cycles found so far

    # Iterate through potential new vertices to add.
    # 'new_node_idx' refers to the 0-indexed label of the vertex currently being considered.
    # The maximum number of vertices is 100, so new_node_idx goes from 0 to 99.
    for new_node_idx in range(100):
        # Calculate how many new triangles would be formed if 'new_node_idx'
        # is connected to ALL previously added 'new_node_idx' vertices (0 to new_node_idx - 1).
        # This number is given by C(new_node_idx, 2) (combinations of 2 from new_node_idx vertices),
        # as each pair of existing vertices connected to 'new_node_idx' forms a triangle.
        # C(n, 2) = n * (n - 1) / 2
        triangles_if_connected_to_all_prev = new_node_idx * (new_node_idx - 1) // 2

        if current_triangles_count + triangles_if_connected_to_all_prev <= k:
            # If connecting 'new_node_idx' to all previous vertices does not exceed 'k' triangles,
            # we fully connect it. This forms a larger complete subgraph.
            
            # Connect 'new_node_idx' to all vertices with indices from 0 to 'new_node_idx - 1'
            for j in range(new_node_idx):
                adj[new_node_idx][j] = adj[j][new_node_idx] = 1
            
            current_triangles_count += triangles_if_connected_to_all_prev
            n_nodes = new_node_idx + 1 # Update the total count of nodes used
            
            if current_triangles_count == k:
                # If we've hit exactly 'k' triangles, we are done.
                # This typically happens when 'k' is the number of triangles in a complete graph K_n.
                break
        else:
            # If connecting 'new_node_idx' to all previous vertices would exceed 'k' triangles,
            # we need to be more selective. This 'new_node_idx' will be the last vertex added.
            # We connect it to a specific number of previous vertices to get exactly the
            # remaining required triangles.
            
            needed_triangles_for_this_node = k - current_triangles_count
            
            m_connections = 0
            # Find the largest 'm_candidate' (number of connections) such that C(m_candidate, 2)
            # is less than or equal to 'needed_triangles_for_this_node'.
            # 'm_candidate' can be at most 'new_node_idx' (number of existing vertices).
            for m_candidate in range(new_node_idx, -1, -1):
                if m_candidate * (m_candidate - 1) // 2 <= needed_triangles_for_this_node:
                    m_connections = m_candidate
                    break
            
            # Connect 'new_node_idx' to the first 'm_connections' existing vertices (0 to m_connections - 1)
            for j in range(m_connections):
                adj[new_node_idx][j] = adj[j][new_node_idx] = 1
            
            current_triangles_count += m_connections * (m_connections - 1) // 2
            n_nodes = new_node_idx + 1 # Update total nodes
            break # Graph constructed with exactly 'k' triangles

    # Format the output as specified: first line is 'n_nodes', then 'n_nodes' lines
    # for the adjacency matrix.
    result_lines = [str(n_nodes)]
    for i in range(n_nodes):
        row_str = "".join(map(str, adj[i][:n_nodes]))
        result_lines.append(row_str)
    
    return result_lines
```