```python
def solve(n, m, edges):
    color = [0] * n
    graph = [[] for _ in range(n)]
    
    for edge in edges:
        u, v = edge[0] - 1, edge[1] - 1
        graph[u].append(v)
        graph[v].append(u)

    for i in range(n):
        for vertex in graph[i]:
            if color[i] == color[vertex]:
                if color[i] == 0:
                    color[vertex] = 1
                else:
                    color[i] = 0

    for i in range(n):
        for vertex in graph[i]:
            if color[i] == color[vertex]:
                return -1

    A = [i + 1 for i in range(n) if color[i] == 0]
    B = [i + 1 for i in range(n) if color[i] == 1]

    return len(A), A, len(B), B
```