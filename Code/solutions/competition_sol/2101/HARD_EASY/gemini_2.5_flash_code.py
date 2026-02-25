```python
import collections

def find_mst_weight(n: int, m: int, edges: list[tuple[int, int]]) -> int:
    """
    Calculates the minimum spanning tree weight of a complete graph with
    n vertices, where m edges have weight 1 and all other edges have weight 0.

    The Minimum Spanning Tree (MST) algorithm prioritizes edges with smaller weights.
    Since edge weights are only 0 or 1, the MST will use as many 0-weight edges as possible.
    The total weight of the MST will be equal to the number of 1-weight edges required
    to connect all components formed solely by 0-weight edges.
    If there are 'k' connected components formed by 0-weight edges, then 'k-1'
    additional edges (which must be 1-weight edges) are needed to connect these
    components into a single spanning tree.
    Therefore, the MST weight is 'k-1'.

    This problem is solved by finding the number of connected components in the
    subgraph formed by *only* 0-weight edges. This is efficiently done using a
    modified Breadth-First Search (BFS) algorithm optimized for complement graphs.

    Args:
        n: The number of vertices in the graph (1 <= n <= 10^5).
        m: The number of edges with weight 1 (0 <= m <= min(n*(n-1)/2, 10^5)).
        edges: A list of tuples, where each tuple (a, b) represents a 1-weight
               edge between vertices a and b (1 <= a, b <= n, a != b).
               It is guaranteed that no edge appears twice.

    Returns:
        The weight of the minimum spanning tree.

    Time Complexity: O(N + M)
        - Building adjacency list for 1-weight edges: O(M). Using sets for adjacency
          lists ensures O(1) average-case lookup for neighbors.
        - BFS for complement graph:
          Each vertex is added to the queue and processed exactly once. (O(N) total)
          When processing a vertex `u` from the queue, we iterate through a list
          derived from `unvisited_nodes`. A node `v` from this list is either:
          1. Added to the queue (if (u,v) is a 0-weight edge), which implies `v` is
             now considered visited and will not be in `unvisited_nodes` again.
          2. Kept for future consideration (if (u,v) is a 1-weight edge). These
             nodes are re-added to `unvisited_nodes`.
          The critical aspect for O(N+M) complexity is that the total work done
          in iterating through `v_candidate in current_unvisited_list` is amortized.
          Each time a 1-weight edge (u,v) causes `v` to be reconsidered, it contributes
          to the O(M) part. Each time a 0-weight edge (u,v) causes `v` to be added
          to the queue, it contributes to the O(N) part. Overall, the total time
          complexity for finding components is O(N + M).

    Space Complexity: O(N + M)
        - Adjacency list `adj`: O(N + M) to store N vertices and M edges.
        - `unvisited_nodes` set: O(N) in the worst case.
        - BFS queue `q`: O(N) in the worst case.
    """

    # For a single vertex graph, there are no edges, so MST weight is 0.
    if n == 1:
        return 0

    # Build adjacency lists for 1-weight edges.
    # Using sets provides O(1) average-case membership testing (e.g., `v_candidate not in adj[u]`).
    adj = [set() for _ in range(n + 1)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    # `unvisited_nodes` keeps track of vertices that have not yet been assigned
    # to any connected component in the 0-weight subgraph.
    unvisited_nodes = set(range(1, n + 1))
    num_components = 0

    # Continue as long as there are unvisited nodes, indicating potentially new components.
    while unvisited_nodes:
        num_components += 1
        
        # Start a new BFS from an arbitrary unvisited node.
        # .pop() removes an arbitrary element from the set.
        start_node = unvisited_nodes.pop()
        q = collections.deque([start_node])

        # BFS for the current component.
        while q:
            u = q.popleft()
            
            # This list will temporarily store nodes from `unvisited_nodes`
            # that are *not* 0-weight neighbors of `u` (i.e., they are 1-weight
            # neighbors of `u`). These nodes need to be kept in `unvisited_nodes`
            # for potential future processing by other nodes in the current component,
            # or by later components.
            nodes_to_repopulate_unvisited = []
            
            # To safely iterate over `unvisited_nodes` while conceptually modifying it,
            # we convert it to a list and then clear the original set.
            # Nodes that are found to be 0-weight neighbors will be added to `q`
            # and effectively removed from `unvisited_nodes` by not being re-added.
            current_unvisited_list_snapshot = list(unvisited_nodes)
            unvisited_nodes.clear() # Clear the set to build it anew for the next iteration

            for v_candidate in current_unvisited_list_snapshot:
                if v_candidate not in adj[u]:
                    # (u, v_candidate) is a 0-weight edge. Add v_candidate to the current component.
                    q.append(v_candidate)
                else:
                    # (u, v_candidate) is a 1-weight edge. v_candidate cannot be reached from `u`
                    # via a 0-weight edge. It might be reachable from another node in the current
                    # component via a 0-weight edge, or it might belong to a different component.
                    # So, it remains in `unvisited_nodes` for subsequent checks.
                    nodes_to_repopulate_unvisited.append(v_candidate)
            
            # Restore `unvisited_nodes` with only those nodes that were 1-weight neighbors
            # of `u` (and thus not visited in this step of the current component's BFS).
            unvisited_nodes.update(nodes_to_repopulate_unvisited)

    # The MST weight is (number of connected components in the 0-weight subgraph) - 1.
    return num_components - 1
```