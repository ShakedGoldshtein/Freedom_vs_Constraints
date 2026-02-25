```python
from collections import deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx]); idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        a -= 1
        b -= 1
        
        graph = [[] for _ in range(n)]
        for __ in range(n-1):
            u = int(data[idx]); idx += 1
            v = int(data[idx]); idx += 1
            u -= 1
            v -= 1
            graph[u].append(v)
            graph[v].append(u)
        
        parent = [-1] * n
        depth = [0] * n
        queue = deque([a])
        parent[a] = a
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if parent[v] == -1:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    queue.append(v)
        
        path = []
        cur = b
        while cur != a:
            path.append(cur)
            cur = parent[cur]
        path.append(a)
        path_set = set(path)
        
        if len(path) > 3:
            results.append("YES")
            continue
        
        deg = [len(graph[i]) for i in range(n)]
        possible = False
        for i in range(n):
            if deg[i] >= 3 and i not in path_set:
                possible = True
                break
        
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
```