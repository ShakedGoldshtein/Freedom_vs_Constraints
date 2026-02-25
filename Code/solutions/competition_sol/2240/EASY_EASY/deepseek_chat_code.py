```python
import sys
sys.setrecursionlimit(300000)

def solve(n, edges, values):
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    stack = [1]
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        for v in graph[u]:
            if v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                stack.append(v)
    
    dp_inc = [0] * (n + 1)
    dp_dec = [0] * (n + 1)
    
    for u in reversed(order):
        if u != 1:
            p = parent[u]
            dp_inc[p] = max(dp_inc[p], dp_inc[u])
            dp_dec[p] = max(dp_dec[p], dp_dec[u])
    
    total_moves = 0
    current = 0
    for u in order:
        if u != 1:
            p = parent[u]
            current_inc = dp_inc[p]
            current_dec = dp_dec[p]
        else:
            current_inc = 0
            current_dec = 0
        
        diff = values[u - 1] + current_inc - current_dec
        if diff > 0:
            dp_dec[u] += diff
        else:
            dp_inc[u] += -diff
        
        total_moves += abs(diff)
    
    return total_moves + abs(values[0] + dp_inc[1] - dp_dec[1])
```