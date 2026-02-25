```python
import collections

def solve(n: int, m: int, edges: list[tuple[int, int]]) -> tuple[list[int], list[int]] | None:
    """
    Finds two disjoint subsets of vertices A and B such that both A and B are vertex covers,
    or determines if it's impossible.

    The problem requires finding two disjoint vertex covers A and B. This implies that
    the graph must be bipartite, with A and B corresponding to the two partitions
    (color classes). If the graph is not bipartite, such sets cannot exist.

    Args:
        n: The number of vertices in the graph (1-indexed, 2 <= n <= 100,000).
        m: The number of edges in the graph (1 <= m <= 100,000).
        edges: A list of tuples (u, v) representing undirected edges.
               The graph is guaranteed not to contain self-loops or multiple edges.

    Returns:
        A tuple of two lists (set_A, set_B) containing the 1-indexed vertices of the
        two disjoint vertex covers. Returns None if it's impossible.
    
    Time Complexity: O(N + M), where N is the number of vertices and M is the number of edges.
                     Graph construction takes O(N+M), and the BFS traversal for 2-coloring
                     visits each vertex and edge at most once.
    Space Complexity: O(N + M) for storing the adjacency list and auxiliary data structures
                      (colors array, queue, result lists).
    """
    
    # Adjacency list for the graph. Vertices are 1-indexed.
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # `colors[i]` stores the color of vertex `i`:
    # 0: uncolored
    # 1: color 1 (vertices assigned this color will be collected into `set_A`)
    # 2: color 2 (vertices assigned this color will be collected into `set_B`)
    colors = [0] * (n + 1)

    set_A = []
    set_B = []

    # Iterate through all vertices to handle disconnected components.
    for i in range(1, n + 1):
        # Process uncolored vertices that are part of an edge.
        # Isolated vertices (adj[i] is empty) are not included in A or B,
        # consistent with the problem example, as they don't need to be covered.
        if colors[i] == 0 and adj[i]:
            
            queue = collections.deque()
            queue.append(i)
            colors[i] = 1 # Start coloring this component with color 1
            
            current_component_color1_vertices = []
            current_component_color2_vertices = []
            current_component_color1_vertices.append(i)

            while queue:
                u = queue.popleft()

                for v in adj[u]:
                    if colors[v] == 0:  # Neighbor 'v' is uncolored
                        colors[v] = 3 - colors[u]  # Assign opposite color
                        if colors[v] == 1:
                            current_component_color1_vertices.append(v)
                        else: # colors[v] == 2
                            current_component_color2_vertices.append(v)
                        queue.append(v)
                    elif colors[v] == colors[u]:  # Neighbor 'v' has same color as 'u'
                        # This indicates an odd-length cycle, meaning the graph is not bipartite.
                        # Therefore, it's impossible to find two such disjoint vertex covers.
                        return None
            
            # After a component is fully colored and confirmed bipartite,
            # extend the global `set_A` and `set_B` with its color classes.
            # The choice of which color class goes to `set_A` and which to `set_B`
            # for any given component is arbitrary, as long as it's consistent.
            # Here, we map 'color 1' vertices to `set_A` and 'color 2' vertices to `set_B`.
            set_A.extend(current_component_color1_vertices)
            set_B.extend(current_component_color2_vertices)

    # Sort the lists for canonical output. While not strictly required by the problem,
    # it often helps with consistency and matches the example's vertex ordering.
    set_A.sort()
    set_B.sort()

    return set_A, set_B
```