```python
def draw_x_shape(n: int) -> str:
    """
    Generates an X-shape pattern of size n x n using '■' and '□' characters.
    The input n must be an odd integer >= 3.

    Args:
        n: An odd integer >= 3 representing the size of the X-shape.

    Returns:
        A string representing the X-shape pattern, with lines separated by '\n'.

    Raises:
        ValueError: If n is not an odd integer >= 3.
    """
    if not isinstance(n, int) or n < 3 or n % 2 == 0:
        raise ValueError("n must be an odd integer >= 3")

    lines = []
    for i in range(n):
        line = []
        for j in range(n):
            if i == j or i + j == n - 1:
                line.append('■')
            else:
                line.append('□')
        lines.append(''.join(line))
    return '\n'.join(lines)
```