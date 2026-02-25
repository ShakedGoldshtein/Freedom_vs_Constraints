```python
def solve(n, matrix, deletions):
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = matrix[i][j]
    
    vertices = [x - 1 for x in deletions[::-1]]
    result = []
    
    for k in range(n):
        vertex_k = vertices[k]
        total = 0
        
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][vertex_k] + dist[vertex_k][j]:
                    dist[i][j] = dist[i][vertex_k] + dist[vertex_k][j]
        
        for i in range(k + 1):
            for j in range(k + 1):
                total += dist[vertices[i]][vertices[j]]
        
        result.append(total)
    
    return result[::-1]
```