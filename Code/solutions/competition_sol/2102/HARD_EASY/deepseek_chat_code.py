```python
def solve(k):
    max_vertices = 100
    adj = [[0] * max_vertices for _ in range(max_vertices)]
    
    n = 0
    while n * (n - 1) * (n - 2) // 6 < k:
        n += 1
    
    for i in range(n):
        for j in range(i + 1, n):
            adj[i][j] = 1
            adj[j][i] = 1
    
    cycles = n * (n - 1) * (n - 2) // 6
    remaining = cycles - k
    
    v = n
    while remaining > 0 and v < max_vertices:
        remove_count = 0
        for u in range(1, n):
            if u * (u - 1) // 2 <= remaining:
                remove_count = u * (u - 1) // 2
            else:
                break
        
        if remove_count == 0:
            break
            
        for u in range(remove_count):
            adj[u][v] = 1
            adj[v][u] = 1
        
        remaining -= remove_count
        v += 1
    
    while remaining > 0:
        found = False
        for i in range(n):
            for j in range(i + 1, n):
                if adj[i][j] == 1:
                    adj[i][j] = 0
                    adj[j][i] = 0
                    remaining -= 1
                    found = True
                    break
            if found:
                break
    
    actual_n = max_vertices
    for i in range(max_vertices):
        if any(adj[i][j] == 1 for j in range(max_vertices)):
            continue
        actual_n = i
        break
    
    result = [str(actual_n)]
    for i in range(actual_n):
        result.append(''.join(str(adj[i][j]) for j in range(actual_n)))
    
    return '\n'.join(result)
```