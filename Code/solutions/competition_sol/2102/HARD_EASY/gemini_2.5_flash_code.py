```python
import math
from typing import List

def solve(k: int) -> List[str]:
    """
    Constructs an undirected graph with exactly k cycles of length 3 (triangles).

    The graph is built by iteratively adding vertices. For each new vertex `v_i`
    (with index `i`), it is connected to a subset of existing vertices `v_0, ..., v_{i-1}`.
    Specifically, it connects `v_i` to the first `m` vertices (`v_0, ..., v_{m-1}`),
    where `m` is the largest integer such that `C(m, 2)` (number of new triangles formed
    by `v_i` and the clique `v_0, ..., v_{m-1}`) plus the `current_triangles` does not
    exceed `k`. This construction ensures that the connected previous vertices always
    form a clique, allowing for precise calculation of new triangles `C(m, 2)`.

    Args:
        k: The desired number of cycles of length 3 (triangles).
           Constraint: 1 <= k <= 10^5.

    Returns:
        A list of strings representing the adjacency matrix of the constructed graph.
        The first string in the list is the total number of vertices `n`.
        Each subsequent string represents a row of the `n x n` adjacency matrix.
    
    Raises:
        ValueError: If k is outside the expected range [1, 10^5].
    """

    if not (1 <= k <= 10**5):
        raise ValueError(f"Input k must be between 1 and 10^5, but got {k}.")

    MAX_VERTICES = 100
    
    adj_matrix = [[0] * MAX_VERTICES for _ in range(MAX_VERTICES)]
    
    num_nodes = 0
    current_triangles = 0

    for new_node_idx in range(MAX_VERTICES):
        
        max_connections_for_new_node = 0
        
        # `j` represents the count of previous vertices (`v_0` through `v_{j-1}`)
        # that `v_{new_node_idx}` will connect to.
        for j in range(new_node_idx + 1):
            # Calculate C(j, 2) which is j * (j - 1) / 2.
            # This is the number of triangles formed by `v_{new_node_idx}` and every pair
            # of vertices within the clique `v_0, ..., v_{j-1}`.
            triangles_if_connect_to_j = j * (j - 1) // 2
            
            if current_triangles + triangles_if_connect_to_j <= k:
                max_connections_for_new_node = j
            else:
                # If connecting to `j` vertices would exceed `k`, then `j-1` was the largest valid count.
                # `max_connections_for_new_node` already holds the `j-1` value from the previous iteration.
                break
        
        num_nodes = new_node_idx + 1

        # Establish edges for `v_{new_node_idx}` with `v_0, ..., v_{max_connections_for_new_node-1}`.
        for p_idx in range(max_connections_for_new_node):
            adj_matrix[new_node_idx][p_idx] = 1
            adj_matrix[p_idx][new_node_idx] = 1
        
        current_triangles += max_connections_for_new_node * (max_connections_for_new_node - 1) // 2
        
        if current_triangles == k:
            break
    
    output_lines = [str(num_nodes)]
    for i in range(num_nodes):
        output_lines.append("".join(map(str, adj_matrix[i][:num_nodes])))
    
    return output_lines
```