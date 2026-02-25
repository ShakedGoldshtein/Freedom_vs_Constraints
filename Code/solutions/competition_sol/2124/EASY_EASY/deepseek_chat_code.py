```python
import sys
from collections import deque

def solve(n, m, x, edges):
    graph = [[] for _ in range(n)]
    for a, b, c in edges:
        graph[a-1].append((b-1, c))
    
    def bfs(capacity):
        parent = [-1] * n
        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        
        while queue:
            u = queue.popleft()
            for v, cap in graph[u]:
                if not visited[v] and cap >= capacity:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    if v == n-1:
                        break
        
        if not visited[n-1]:
            return 0.0
        
        path_flow = float('inf')
        v = n-1
        while v != 0:
            u = parent[v]
            for neighbor, cap in graph[u]:
                if neighbor == v:
                    path_flow = min(path_flow, cap)
                    break
            v = u
        
        v = n-1
        while v != 0:
            u = parent[v]
            for i, (neighbor, cap) in enumerate(graph[u]):
                if neighbor == v:
                    graph[u][i] = (neighbor, cap - path_flow)
                    break
            found = False
            for i, (neighbor, cap) in enumerate(graph[v]):
                if neighbor == u:
                    graph[v][i] = (neighbor, cap + path_flow)
                    found = True
                    break
            if not found:
                graph[v].append((u, path_flow))
            v = u
        
        return path_flow
    
    def max_flow():
        total_flow = 0.0
        while True:
            flow = bfs(1e-9)
            if flow <= 0:
                break
            total_flow += flow
        return total_flow
    
    low, high = 0.0, 1e9
    for _ in range(100):
        mid = (low + high) / 2.0
        temp_graph = [list(adj) for adj in graph]
        
        total = max_flow()
        graph = temp_graph
        
        if total >= x * mid:
            low = mid
        else:
            high = mid
    
    return low * x
```