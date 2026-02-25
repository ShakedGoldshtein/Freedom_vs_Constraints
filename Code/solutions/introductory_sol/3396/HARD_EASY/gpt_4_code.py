```python
def sum_matrices(matrix1, matrix2):
    try:
        # The matrix to store the result
        sum_matrix = []

        # Check if both matrices are square
        if len(matrix1) != len(matrix1[0]) or len(matrix2) != len(matrix2[0]):
            return "Input matrices must be square"

        # Iterate over rows
        for i in range(len(matrix1)):
            row = []

            # Iterate over columns
            for j in range(len(matrix1[i])):
                # Add the numbers at the same position in the two matrices
                row.append(matrix1[i][j] + matrix2[i][j])

            sum_matrix.append(row)

        return sum_matrix

    except Exception as e:
        return str(e)
```