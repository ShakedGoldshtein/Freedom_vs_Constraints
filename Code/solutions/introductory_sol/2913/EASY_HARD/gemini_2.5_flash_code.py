```python
def draw_x_shape(n: int) -> str:
    """
    Draws an X-shape using '■' and '□' characters for a given odd integer n.

    Args:
        n: An odd integer (>= 3) representing the size of the square grid.

    Returns:
        A string representing the X-shape, with lines separated by '\n'.
    """
    grid_lines = []
    for r in range(n):
        current_line_chars = []
        for c in range(n):
            if r == c or r + c == n - 1:
                current_line_chars.append('■')
            else:
                current_line_chars.append('□')
        grid_lines.append("".join(current_line_chars))
    return "\n".join(grid_lines)
```