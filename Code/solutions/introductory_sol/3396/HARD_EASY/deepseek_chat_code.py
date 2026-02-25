```python
def matrix_sum(matrix_a, matrix_b):
    """
    Compute the sum of two square matrices of the same dimensions.
    
    Args:
        matrix_a: First N x N matrix of integers
        matrix_b: Second N x N matrix of integers
    
    Returns:
        N x N matrix representing the element-wise sum of matrix_a and matrix_b
    
    Raises:
        ValueError: If matrices are not square or have different dimensions
        TypeError: If inputs are not valid matrices
    """
    if not matrix_a or not matrix_b:
        raise ValueError("Both matrices must be non-empty")
    
    n = len(matrix_a)
    
    # Validate matrix dimensions and structure
    if not all(len(row) == n for row in matrix_a):
        raise ValueError("First matrix is not square")
    
    if len(matrix_b) != n:
        raise ValueError("Matrices have different dimensions")
    
    if not all(len(row) == n for row in matrix_b):
        raise ValueError("Second matrix is not square")
    
    # Initialize result matrix
    result = [[0] * n for _ in range(n)]
    
    # Perform element-wise addition
    for i in range(n):
        for j in range(n):
            # Validate element types
            if not isinstance(matrix_a[i][j], (int, float)) or not isinstance(matrix_b[i][j], (int, float)):
                raise TypeError("Matrix elements must be numeric")
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
    
    return result
```