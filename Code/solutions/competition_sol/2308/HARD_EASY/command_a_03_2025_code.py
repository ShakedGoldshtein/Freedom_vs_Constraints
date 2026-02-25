```python
def solve(n: int, w: int, arrays: list[list[int]]) -> list[int]:
    """
    Calculate the maximum sum of integers in each column for a given table.

    Args:
        n (int): Number of arrays.
        w (int): Width of the table.
        arrays (list of list of int): List of arrays, where each array is a list of integers.

    Returns:
        list of int: Maximum sum for each column from 1 to w.
    """
    # Initialize the result array with zeros
    result = [0] * w

    # Iterate over each column
    for j in range(w):
        max_sum = 0
        # Iterate over each array
        for i in range(n):
            l_i = len(arrays[i])
            # Calculate the possible starting positions for the array in the current column
            start_pos = max(0, j - l_i + 1)
            end_pos = min(w - l_i, j) + 1
            # Iterate over possible starting positions
            for k in range(start_pos, end_pos):
                # Calculate the sum of the array segment that aligns with the current column
                current_sum = sum(arrays[i][max(0, j - k) : min(l_i, j - k + l_i)])
                # Update the maximum sum for the current column
                max_sum = max(max_sum, current_sum)
        # Store the maximum sum for the current column in the result
        result[j] = max_sum

    return result
```