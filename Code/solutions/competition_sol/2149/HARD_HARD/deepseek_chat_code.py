```python
def solve(n, m, a_list):
    if m == 0:
        return 0
    
    if n == 0:
        return 1 if 0 in a_list else 0
    
    full_mask = (1 << n) - 1
    
    visited = [False] * (1 << n)
    has_element = [False] * (1 << n)
    
    for a in a_list:
        has_element[a] = True
    
    def dfs(node):
        stack = [node]
        visited[node] = True
        
        while stack:
            current = stack.pop()
            
            if has_element[current]:
                for neighbor in get_neighbors(current):
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
    
    def get_neighbors(x):
        neighbors = []
        
        complement = full_mask & (~x)
        current = complement
        
        while True:
            if has_element[current]:
                neighbors.append(current)
            if current == 0:
                break
            current = (current - 1) & complement
    
        return neighbors
    
    components = 0
    for a in a_list:
        if not visited[a]:
            components += 1
            dfs(a)
    
    return components
```