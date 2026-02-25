```python
def solve(n: int, m: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    """
    Solves the problem of splitting a graph into two disjoint vertex covers.

    Args:
        n (int): The number of vertices in the graph.
        m (int): The number of edges in the graph.
        edges (list of tuples): A list of edges, where each edge is represented as a tuple (u, v).

    Returns:
        list of lists: A list containing two lists, each representing a vertex cover.
                       If it's impossible to split the graph, returns [[-1]].
    """
    # Create an adjacency list to represent the graph
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Check if the graph is bipartite using BFS
    color = [0] * (n + 1)
    possible = True
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            queue = [i]
            while queue:
                node = queue.pop(0)
                for neighbor in adj[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        possible = False
                        break
                if not possible:
                    break
            if not possible:
                break

    if not possible:
        return [[-1]]

    # Split vertices into two sets based on their color
    set_a = [i for i in range(1, n + 1) if color[i] == 1]
    set_b = [i for i in range(1, n + 1) if color[i] == 2]

    # Check if both sets are vertex covers
    def is_vertex_cover(s: list[int], adj: list[list[int]]) -> bool:
        """
        Checks if a given set of vertices is a vertex cover.

        Args:
        s (list): A list of vertices.
        adj (list of lists): The adjacency list representing the graph.

        Returns:
        bool: True if the set is a vertex cover, False otherwise.
        """
        for u in range(1, n + 1):
            for v in adj[u]:
                if u < v and v not in s and u not in s:
                    return False
        return True

    if not is_vertex_cover(set_a, adj) or not is_vertex_cover(set_b, adj):
        return [[-1]]

    # Return the two vertex covers
    return [sorted(set_a), sorted(set_b)]
```