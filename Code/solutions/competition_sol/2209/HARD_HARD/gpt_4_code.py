```python
from collections import defaultdict, deque

def min_and_max_weights(n, edges):
    conns = defaultdict(list)
    for v1, v2 in edges:
        conns[v1].append(v2)
        conns[v2].append(v1)

    dist = [0]*(n+1)
    leaves = [True]*(n+1)

    q = deque([1])
    visited = [0]*(n+1)
    visited[1] = 1

    while q:
        u = q.popleft()

        for v in conns[u]:
            if not visited[v]:
                visited[v] = 1
                dist[v] = dist[u] + 1
                q.append(v)
            else:
                leaves[u] &= (len(conns[u]) == 1) 
                leaves[v] &= (len(conns[v]) == 1)

    odd, even = 0, 0
    for i in range(1, n+1):
        if leaves[i]:
            if dist[i] % 2 == 0:
                even += 1
            else:
                odd += 1

    min_result = 1 if odd == 0 else 3
    max_result = n - 1 - (odd or even) + max(odd, even)
    return min_result, max_result
```
