```python
def solve(n: int, m: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    """
    Solves the problem of splitting a graph into two disjoint vertex covers.

    Args:
        n (int): Number of vertices in the graph.
        m (int): Number of edges in the graph.
        edges (list of tuples): List of edges, where each edge is a tuple of two vertices.

    Returns:
        list: A list containing two lists of vertices, each representing a vertex cover.
              If it's impossible to split the graph, returns [[-1]].
    """
    if n < 2 or m < 1:
        return [[-1]]

    # Build adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Check if the graph is bipartite
    color = [0] * (n + 1)
    possible = True
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            stack = [i]
            while stack:
                node = stack.pop()
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - color[node]
                        stack.append(neighbor)
                    elif color[neighbor] == color[node]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break

    if not possible:
        return [[-1]]

    # Split vertices into two sets based on color
    set_a = [i for i in range(1, n + 1) if color[i] == 1]
    set_b = [i for i in range(1, n + 1) if color[i] == 2]

    # Check if both sets are vertex covers
    def is_vertex_cover(vertices: list[int], edges: list[tuple[int, int]]) -> bool:
        """
        Checks if a given set of vertices is a vertex cover.

        Args:
            vertices (list): List of vertices to check.
            edges (list of tuples): List of edges in the graph.

        Returns:
            bool: True if the set is a vertex cover, False otherwise.
        """
        for u, v in edges:
            if u not in vertices and v not in vertices:
                return False
        return True

    if not is_vertex_cover(set_a, edges) or not is_vertex_cover(set_b, edges):
        return [[-1]]

    return [sorted(set_a), sorted(set_b)]
```