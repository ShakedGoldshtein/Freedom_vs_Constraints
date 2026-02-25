```python
from collections import deque
from sys import setrecursionlimit, maxsize

setrecursionlimit(int(1e6))


def solve(t, test_cases):
    def BFS(x, y):
        dist[y] = [0, y]
        q = deque([y])
        while q:
            x = q.popleft()
            for y in graph[x]:
                if y == dist[x][1]: continue
                dist[y] = [dist[x][0] + 1, x]
                q.append(y)

    res = []
    for _ in range(t):
        n, a, b, edges = test_cases[_]
        graph = [[] for _ in range(n+1)]
        dist = [[-1, -1] for _ in range(n+1)]
        depth = [0] * (n+1)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        BFS(0, a)
        path = [b]
        while path[-1] != a: path.append(dist[path[-1]][1])
        for i in range(1, len(path)):
            depth[path[i]] = max(depth[path[i]], min(i, len(path) - i))
        BFS(0, path[len(path) // 2])
        top = max(dist)
        BFS(0, top[1])
        res.append("YES" if max(dist)[0] <= 2 * depth[top[1]] else "NO")

    return res
```