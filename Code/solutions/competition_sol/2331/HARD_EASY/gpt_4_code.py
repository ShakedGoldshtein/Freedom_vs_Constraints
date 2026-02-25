Here is the Python code for this:

```python
from collections import deque

def add_edge(u, v):
    graph[u].append((v, len(graph[v])))
    graph[v].append((u, len(graph[u]) - 1))

t = int(input().strip())
for _ in range(t):
    n, a, b = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    dp = [0] * (n + 1)
    Max = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        add_edge(u, v)
    start = a
    q = deque([start])
    vis = [0] * (n + 1)
    vis[start] = 1
    while len(q) > 0:
        v = q.pop()
        for u, rev in graph[v]:
            if vis[u] == 0:
                q.appendleft(u)
                vis[u] = 1
                Max[u] = max(Max[u], dp[u])
                for to, revv in graph[u]:
                    if to != v:
                        graph[to].pop(revv)
                        dp[to] = max(dp[to], min(dp[v], Max[v]) + 1)
    Max[b] = max(Max[b], dp[b])
    if max(Max) * 2 < n:
        print('NO')
    else:
        print('YES')
```

On an overview, it's a depth-first-based solution to get maximum depth and update dp values. Then, check whether maximum nodes reachable in both directions of a node is at least half of nodes or not. If it's at least half, return 'YES', else return 'NO'.