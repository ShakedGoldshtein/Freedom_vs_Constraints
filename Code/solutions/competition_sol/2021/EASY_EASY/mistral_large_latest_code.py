```python
def solve(n, m, edges):
    from collections import defaultdict

    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Check if the graph is bipartite and find the bipartition
    color = [-1] * (n + 1)
    is_bipartite = True

    def dfs(u, c):
        nonlocal is_bipartite
        color[u] = c
        for v in adj[u]:
            if color[v] == -1:
                dfs(v, c ^ 1)
            elif color[v] == c:
                is_bipartite = False

    for u in range(1, n + 1):
        if color[u] == -1:
            dfs(u, 0)
            if not is_bipartite:
                return [-1]

    # The two partitions are the vertex covers
    cover1 = [u for u in range(1, n + 1) if color[u] == 0]
    cover2 = [u for u in range(1, n + 1) if color[u] == 1]

    return [
        [len(cover1), cover1],
        [len(cover2), cover2]
    ]
```