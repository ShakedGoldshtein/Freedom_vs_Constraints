```python
def solve(matrix1, matrix2):
    n = len(matrix1)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result
```