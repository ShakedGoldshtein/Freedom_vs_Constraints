```python
def matrix_addition(matrix1, matrix2):
    n = len(matrix1)
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result
```