```python
from collections import deque

def find_vertex_covers(n, edges):
    """
    Finds two disjoint vertex covers for the given undirected graph or returns -1 if impossible.

    Args:
        n: Number of vertices (1-based indexing).
        edges: List of tuples representing undirected edges (u, v).

    Returns:
        -1 if impossible, otherwise a tuple of two lists representing the vertex covers.
    """
    if n < 2 or not edges:
        return -1

    # Build adjacency list and degree count
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # Check if the graph is bipartite (2-colorable)
    color = [-1] * (n + 1)
    is_bipartite = True
    q = deque()

    for i in range(1, n + 1):
        if color[i] == -1:
            q.append(i)
            color[i] = 0
            while q and is_bipartite:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break

    if not is_bipartite:
        return -1

    # The two color classes form the vertex covers
    cover_a = [i for i in range(1, n + 1) if color[i] == 0]
    cover_b = [i for i in range(1, n + 1) if color[i] == 1]

    # Verify both covers are valid (should be true for bipartite graphs)
    def is_valid_cover(cover):
        covered_edges = set()
        for u in cover:
            for v in adj[u]:
                if u < v:
                    covered_edges.add((u, v))
                else:
                    covered_edges.add((v, u))
        return len(covered_edges) == len(edges)

    if not (is_valid_cover(cover_a) and is_valid_cover(cover_b)):
        return -1

    return (cover_a, cover_b)

def format_output(result):
    """
    Formats the result into the required output format.
    """
    if result == -1:
        return "-1"
    cover_a, cover_b = result
    output = []
    output.append(f"{len(cover_a)}")
    output.append(" ".join(map(str, cover_a)))
    output.append(f"{len(cover_b)}")
    output.append(" ".join(map(str, cover_b)))
    return "\n".join(output)

def solve(n, m, edges):
    """
    Main function to solve the problem. Takes n, m, and edges as input and returns the formatted output.
    """
    result = find_vertex_covers(n, edges)
    return format_output(result)
```