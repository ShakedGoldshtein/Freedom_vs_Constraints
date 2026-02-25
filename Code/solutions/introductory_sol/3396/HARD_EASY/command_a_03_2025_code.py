```python
def add_matrices(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    """
    Adds two square matrices element-wise.

    Args:
        matrix1 (list of lists): First square matrix of integers.
        matrix2 (list of lists): Second square matrix of integers.

    Returns:
        list of lists: Resulting matrix after element-wise addition.

    Raises:
        ValueError: If matrices are not square or of different sizes.
    """
    # Check if matrices are square and of the same size
    if not matrix1 or not matrix2:
        raise ValueError("Matrices cannot be empty")

    n = len(matrix1)
    if len(matrix2) != n or any(len(row) != n for row in matrix1) or any(len(row) != n for row in matrix2):
        raise ValueError("Matrices must be square and of the same size")

    # Perform element-wise addition
    return [[matrix1[i][j] + matrix2[i][j] for j in range(n)] for i in range(n)]
```