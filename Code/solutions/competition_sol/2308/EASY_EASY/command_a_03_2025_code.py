```python
def solve(n: int, w: int, arrays: list[list[int]]) -> list[int]:
    """
    Calculate the maximum sum of integers in each column for a given table with sliding arrays.

    Args:
        n (int): Number of arrays.
        w (int): Width of the table.
        arrays (list of list of int): List of arrays where each array is represented as [length, a1, a2, ..., al].

    Returns:
        list of int: Maximum sum for each column from 1 to w.
    """
    # Initialize a list to store the maximum sum for each column
    max_sums = [0] * w

    # Iterate over each array
    for array in arrays:
        # Extract the length and elements of the array
        length = array[0]
        elements = array[1:]

        # Iterate over each possible starting position of the array in the table
        for start in range(w - length + 1):
            # Calculate the end position of the array
            end = start + length

            # Iterate over each column in the range of the array
            for j in range(start, end):
                # Update the maximum sum for the current column
                max_sums[j] = max(max_sums[j], elements[j - start])

    return max_sums
```