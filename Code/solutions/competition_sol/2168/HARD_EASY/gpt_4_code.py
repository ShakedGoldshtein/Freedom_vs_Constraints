```python
def solve(n, graph, x):
    res = [0] * n

    x = [i-1 for i in x]
    x = list(reversed(x))

    used = [False] * n

    for i in range(n):
        v = x[i]
        used[v] = True
        for u in range(n):
            for w in range(n):
                if graph[u][v] + graph[v][w] < graph[u][w]:
                    graph[u][w] = graph[u][v] + graph[v][w]
        for u in range(n):
            if used[u]:
                for w in range(n):
                    if used[w]:
                        res[i] += graph[u][w]

    return list(reversed(res))
```