```python
import collections

def get_mst_weight(n: int, m: int, edges: list[tuple[int, int]]) -> int:
    """
    Calculates the minimum spanning tree weight of a complete graph with N vertices.
    Edges have weight 0 or 1. Exactly M edges have weight 1, others have weight 0.

    Args:
        n: The number of vertices in the graph.
        m: The number of edges with weight 1.
        edges: A list of tuples, where each tuple (u, v) represents an edge
               of weight 1 between vertices u and v.

    Returns:
        The weight of the minimum spanning tree.
    """
    if n == 1:
        return 0

    # Build an adjacency list for edges of weight 1.
    # Using sets for O(1) average time complexity for 'in' checks.
    adj_1 = {i: set() for i in range(1, n + 1)}
    for u, v in edges:
        adj_1[u].add(v)
        adj_1[v].add(u)

    # `unvisited_nodes` stores all vertices that have not yet been included
    # in any connected component formed by 0-weight edges.
    unvisited_nodes = set(range(1, n + 1))
    
    num_components = 0

    # Perform BFS to find connected components formed exclusively by 0-weight edges.
    while unvisited_nodes:
        num_components += 1
        
        # Start a new BFS from an arbitrary unvisited node.
        # `pop()` removes and returns an arbitrary element from the set.
        start_node = unvisited_nodes.pop() 
        q = collections.deque([start_node])

        # BFS for the current component
        while q:
            u = q.popleft()
            
            # `forbidden_neighbors` are nodes connected to `u` by a 1-weight edge.
            # Any node not in this set and still in `unvisited_nodes` is connected
            # to `u` by a 0-weight edge.
            forbidden_neighbors = adj_1[u]
            
            # Collect nodes from `unvisited_nodes` that are connected to `u` by a 0-weight edge.
            # These nodes will be added to the current component and explored further.
            nodes_to_visit_next = []
            
            # This loop is the core of the optimized BFS for dense graphs/sparse complements.
            # It iterates through the current set of `unvisited_nodes`.
            # A temporary list `nodes_to_visit_next` is used to collect nodes to move,
            # avoiding modification of `unvisited_nodes` during iteration.
            for v_node in unvisited_nodes:
                if v_node not in forbidden_neighbors:
                    nodes_to_visit_next.append(v_node)
            
            # Now, add the identified 0-neighbors to the queue and remove them from `unvisited_nodes`.
            for v_node in nodes_to_visit_next:
                unvisited_nodes.remove(v_node)
                q.append(v_node)

    # The MST weight is determined by the number of connected components formed
    # by 0-weight edges. If there are 'k' such components, we need 'k-1'
    # 1-weight edges to connect them into a single spanning tree.
    # The 0-weight edges within components cost nothing.
    return num_components - 1
```