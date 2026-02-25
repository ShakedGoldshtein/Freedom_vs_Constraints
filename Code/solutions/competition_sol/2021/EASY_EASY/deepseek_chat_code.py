```python
import sys
sys.setrecursionlimit(300000)

def solve(n, m, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] != -1:
            continue
        stack = [i]
        color[i] = 0
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    stack.append(v)
                elif color[v] == color[u]:
                    return "-1"
    
    count0 = color.count(0)
    count1 = n - count0
    
    if count0 == 0 or count1 == 0:
        return "-1"
    
    result = []
    result.append(str(count0))
    result.append(' '.join(str(i) for i in range(1, n + 1) if color[i] == 0))
    result.append(str(count1))
    result.append(' '.join(str(i) for i in range(1, n + 1) if color[i] == 1))
    
    return '\n'.join(result)
```