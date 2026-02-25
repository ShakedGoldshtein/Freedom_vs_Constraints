```python
def sum_matrices(matrix1, matrix2):
    """
    Sums two square matrices of the same size.

    Args:
        matrix1: A list of lists representing the first N x N matrix.
        matrix2: A list of lists representing the second N x N matrix.

    Returns:
        A new N x N matrix (list of lists) representing the sum of matrix1 and matrix2.
    """
    n = len(matrix1)
    
    # Initialize the result matrix with zeros
    result_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Iterate through rows and columns to sum corresponding elements
    for i in range(n):
        for j in range(n):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
            
    return result_matrix
```