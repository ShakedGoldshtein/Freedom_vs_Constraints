```python
from collections import deque

def solve(n, edges, values):
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    queue = deque([1])
    parent[1] = 0
    depth[1] = 0
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                queue.append(v)
    
    operations = [0] * (n + 1)
    operations[1] = values[0]
    
    for i in range(2, n + 1):
        operations[i] = values[i - 1] - values[parent[i] - 1]
    
    total_moves = 0
    for i in range(1, n + 1):
        total_moves += abs(operations[i])
    
    return total_moves
```