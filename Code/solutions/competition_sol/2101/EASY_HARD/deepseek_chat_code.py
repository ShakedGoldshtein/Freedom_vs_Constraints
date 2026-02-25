```python
def solve(n, m, edges=None):
    if m == 0:
        return 0
    
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a-1].add(b-1)
        adj[b-1].add(a-1)
    
    unvisited = set(range(n))
    comp_count = 0
    for i in range(n):
        if i in unvisited:
            comp_count += 1
            stack = [i]
            unvisited.remove(i)
            while stack:
                u = stack.pop()
                neighbors = list(unvisited - adj[u])
                for v in neighbors:
                    unvisited.remove(v)
                    stack.append(v)
    
    return comp_count - 1
```