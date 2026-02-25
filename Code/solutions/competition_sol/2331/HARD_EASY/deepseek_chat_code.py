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
        
        def bfs(start):
            dist = [-1] * n
            dist[start] = 0
            q = deque([start])
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
            return dist
        
        dist_a = bfs(a)
        dist_b = bfs(b)
        
        path = []
        u = b
        while u != a:
            path.append(u)
            for v in graph[u]:
                if dist_a[v] == dist_a[u] - 1:
                    u = v
                    break
        path.append(a)
        path.reverse()
        
        m = len(path)
        if m <= 3:
            results.append("NO")
            continue
        
        def find_farthest(start, avoid1, avoid2):
            dist = [-1] * n
            dist[start] = 0
            q = deque([start])
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if dist[v] == -1 and v != avoid1 and v != avoid2:
                        dist[v] = dist[u] + 1
                        q.append(v)
            max_dist = -1
            farthest = start
            for i in range(n):
                if dist[i] > max_dist:
                    max_dist = dist[i]
                    farthest = i
            return farthest, max_dist
        
        def get_diameter(start, avoid1, avoid2):
            far1, _ = find_farthest(start, avoid1, avoid2)
            far2, diameter = find_farthest(far1, avoid1, avoid2)
            return diameter
        
        head = a
        tail = b
        mid1 = path[m//2 - 1]
        mid2 = path[m//2]
        
        diam1 = get_diameter(head, mid1, mid2)
        diam2 = get_diameter(tail, mid1, mid2)
        
        if diam1 >= m - 1 or diam2 >= m - 1:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
```