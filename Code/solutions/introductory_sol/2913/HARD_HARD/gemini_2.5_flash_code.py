```python
def draw_x_shape(n: int) -> str:
    """
    Generates an 'X' shape as a multiline string using specified characters.

    The 'X' is formed by placing '■' characters along the main diagonal (row == col)
    and the anti-diagonal (row + col == n - 1) of an n x n grid. All other positions
    are filled with '□' characters. Each line of the shape is separated by '\n'.

    Args:
        n: An odd integer representing the dimension of the square grid.
           Must be an integer greater than or equal to 3, and odd.

    Returns:
        A string representing the 'X' shape, with lines separated by newlines.

    Raises:
        ValueError: If `n` is not an integer, less than 3, or an even number.
    """
    # Validate input 'n' to ensure it meets the problem's constraints.
    if not isinstance(n, int):
        raise ValueError("Input 'n' must be an integer.")
    if n < 3:
        raise ValueError("Input 'n' must be an integer greater than or equal to 3.")
    if n % 2 == 0:
        raise ValueError("Input 'n' must be an odd integer.")

    shape_rows = []
    # Iterate through each row of the n x n grid.
    for r in range(n):
        current_row_chars = []
        # Iterate through each column in the current row.
        for c in range(n):
            # A character is part of the 'X' if it lies on the main diagonal (r == c)
            # or the anti-diagonal (r + c == n - 1).
            if r == c or r + c == n - 1:
                current_row_chars.append('■')
            else:
                current_row_chars.append('□')
        # Join the characters for the current row into a single string.
        shape_rows.append("".join(current_row_chars))

    # Join all row strings with newline characters to form the final multiline string.
    return "\n".join(shape_rows)
```