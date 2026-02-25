```python
def solve():
    import sys
    sys.setrecursionlimit(30000)
    input = sys.stdin.read
    data = input().split()
    idx = 0
    
    N = int(data[idx]); idx += 1
    sweetness = [0] * (N + 1)
    for i in range(1, N + 1):
        sweetness[i] = int(data[idx]); idx += 1
    
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        graph[u].append(v)
        graph[v].append(u)
    
    Q = int(data[idx]); idx += 1
    
    parent = [0] * (N + 1)
    depth = [0] * (N + 1)
    stack = [1]
    parent[1] = -1
    while stack:
        u = stack.pop()
        for v in graph[u]:
            if v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                stack.append(v)
    
    results = []
    for _ in range(Q):
        query_type = int(data[idx]); idx += 1
        if query_type == 1:
            node = int(data[idx]); idx += 1
            total = 0
            while node != -1:
                total += sweetness[node]
                node = parent[node]
            results.append(str(total))
        else:
            node = int(data[idx]); idx += 1
            new_sweetness = int(data[idx]); idx += 1
            sweetness[node] = new_sweetness
    
    return "\n".join(results)
```