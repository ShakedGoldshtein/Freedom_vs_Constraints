```python
def solve(n, m, a):
    if m == 0:
        return 0
        
    total = 1 << n
    mask = total - 1
    
    visited = [False] * total
    has_element = [False] * total
    
    for x in a:
        has_element[x] = True
    
    def dfs(x):
        stack = [x]
        visited[x] = True
        while stack:
            u = stack.pop()
            if has_element[u]:
                for v in [u ^ (1 << i) for i in range(n)]:
                    if not visited[v] and has_element[v]:
                        visited[v] = True
                        stack.append(v)
            comp = mask & (~u)
            v = comp
            while True:
                if has_element[v] and not visited[v]:
                    visited[v] = True
                    stack.append(v)
                if v == 0:
                    break
                v = (v - 1) & comp
    
    components = 0
    for x in a:
        if not visited[x]:
            components += 1
            dfs(x)
    
    return components
```