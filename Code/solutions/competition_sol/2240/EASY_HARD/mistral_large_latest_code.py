```python
import sys
from collections import deque

def solve(n, edges, v):
    adj = [[] for _ in range(n+1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    q = deque([1])
    parent[1] = 0
    while q:
        u = q.popleft()
        for node in adj[u]:
            if parent[node] == 0 and node != parent[u]:
                parent[node] = u
                depth[node] = depth[u] + 1
                q.append(node)

    res = 0
    for i in range(1, n+1):
        res += abs(v[i-1]) * (depth[i] + 1)
    return res
```