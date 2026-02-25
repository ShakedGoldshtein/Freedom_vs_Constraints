```python
import sys
from collections import defaultdict, deque

def solve(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    deg = [0] * (n + 1)
    for i in range(1, n + 1):
        deg[i] = len(graph[i])
    
    leaves = [i for i in range(1, n + 1) if deg[i] == 1]
    
    if n == 3:
        return (1, 1)
    
    max_f = n - 1
    min_f = 1
    
    leaf_neighbors = set()
    for leaf in leaves:
        leaf_neighbors.add(graph[leaf][0])
    
    if len(leaves) == 2:
        return (1, 1)
    
    for node in range(1, n + 1):
        leaf_count = 0
        for neighbor in graph[node]:
            if deg[neighbor] == 1:
                leaf_count += 1
        if leaf_count > 1:
            max_f -= (leaf_count - 1)
    
    visited = [False] * (n + 1)
    def dfs(u, parent):
        nonlocal min_f
        leaf_child = 0
        for v in graph[u]:
            if v == parent:
                continue
            if deg[v] == 1:
                leaf_child += 1
            else:
                dfs(v, u)
        if leaf_child > 0:
            min_f += 1
    
    root = 1
    while deg[root] == 1:
        root += 1
    
    min_f = 1
    stack = [(root, -1)]
    while stack:
        u, parent = stack.pop()
        leaf_count = 0
        for v in graph[u]:
            if v == parent:
                continue
            if deg[v] == 1:
                leaf_count += 1
            else:
                stack.append((v, u))
        if leaf_count > 0:
            min_f += 1
    
    min_f = 1 if min_f == 2 else min_f
    
    return (min_f, max_f)

if __name__ == "__main__":
    data = sys.stdin.read().split()
    n = int(data[0])
    edges = []
    index = 1
    for i in range(n - 1):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    res = solve(n, edges)
    print(f"{res[0]} {res[1]}")
```