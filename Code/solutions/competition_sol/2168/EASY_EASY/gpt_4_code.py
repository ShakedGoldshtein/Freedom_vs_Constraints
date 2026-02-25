```python
def solve(n, matrix, vertices):
    vertices = [x-1 for x in vertices]
    vertices.reverse()
    result = [0]*n
    for k in range(n):
        x = vertices[k]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][x] + matrix[x][j])
        for i in vertices[:k+1]:
            for j in vertices[:k+1]:
                if i!=j:
                    result[k] += matrix[j][i]
    return result[::-1]
```