```python
def solve(n, m, edges):
    from collections import deque
    
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * (n + 1)
    
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
            
        q = deque([start])
        color[start] = 0
        
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    return "-1"
    
    count_color_0 = color.count(0)
    count_color_1 = n - count_color_0
    
    if count_color_0 == 0 or count_color_1 == 0:
        return "-1"
    
    result = []
    
    result.append(str(count_color_0))
    vertices_0 = [str(i) for i in range(1, n + 1) if color[i] == 0]
    result.append(" ".join(vertices_0))
    
    result.append(str(count_color_1))
    vertices_1 = [str(i) for i in range(1, n + 1) if color[i] == 1]
    result.append(" ".join(vertices_1))
    
    return "\n".join(result)
```