```python
def solve(n: int, m: int) -> list[tuple[int, int]]:
    """
    Finds a path to visit every cell in an n x m grid exactly once,
    starting from (1, 1), such that all jump vectors are distinct.

    The solution constructs a path by interleaving cells from
    a lexicographically sorted list of all grid cells and its reverse.
    This pattern ensures all cells are visited and generates distinct vectors.

    Args:
        n: The number of rows (1-indexed, 1 <= x <= n).
        m: The number of columns (1-indexed, 1 <= y <= m).
           The product n * m is guaranteed to be between 1 and 10^6.

    Returns:
        A list of (row, col) tuples representing the path.
        Each tuple (x_i, y_i) indicates the i-th cell visited.
        The problem implies that a solution always exists under the given constraints,
        and this constructive algorithm always finds one.
    """

    # Generate all cells in lexicographical order (row-major).
    # Cells are 1-indexed as per problem statement.
    all_cells = []
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            all_cells.append((r, c))

    # Construct the path by interleaving cells from the beginning
    # and end of the `all_cells` list.
    path = []
    left_ptr = 0
    right_ptr = len(all_cells) - 1

    while left_ptr <= right_ptr:
        # Add the cell from the beginning of the `all_cells` list.
        path.append(all_cells[left_ptr])
        
        # If the left and right pointers point to different cells,
        # add the cell from the end of the `all_cells` list.
        # This prevents adding the middle cell twice when n*m is odd.
        if left_ptr != right_ptr:
            path.append(all_cells[right_ptr])
        
        # Move pointers towards the center for the next iteration.
        left_ptr += 1
        right_ptr -= 1

    return path
```