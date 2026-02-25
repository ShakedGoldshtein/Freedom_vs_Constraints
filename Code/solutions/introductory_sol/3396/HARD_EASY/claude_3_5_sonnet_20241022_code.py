```python
def sum_matrices(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    """
    Calculate the sum of two square matrices.
    
    Args:
        matrix1: First square matrix (N x N array of integers)
        matrix2: Second square matrix (N x N array of integers)
        
    Returns:
        Result matrix containing the sum of the two input matrices
    """
    n = len(matrix1)
    result = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
            
    return result
```