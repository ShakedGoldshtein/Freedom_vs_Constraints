```python
def solve(n, m):
    """
    Generates a path to visit all cells in an n x m grid exactly once,
    starting at (1, 1), such that all jump vectors are unique.

    The solution uses a constructive approach by alternating between
    cells from the beginning and end of a lexicographically sorted list
    of all grid cells. This method is known to always produce a valid path
    for any n, m >= 1.

    Args:
        n (int): The number of rows in the grid.
        m (int): The number of columns in the grid.

    Returns:
        list[list[int]]: A list of [x, y] pairs representing the coordinates
                         of the cells in the order they are visited.
                         The problem statement implies that a solution
                         always exists for n, m >= 1, so "-1" is not returned.
    """
    
    num_cells = n * m

    # Generate all cells in lexicographical order (1-indexed coordinates)
    # Example: for n=2, m=2, cells will be [[1,1], [1,2], [2,1], [2,2]]
    cells = [[r, c] for r in range(1, n + 1) for c in range(1, m + 1)]

    path = []
    
    # Use two pointers to alternate picking cells from the start and end of the 'cells' list
    left_ptr = 0
    right_ptr = num_cells - 1

    while left_ptr <= right_ptr:
        # Pick the cell with the smallest coordinates (from the left pointer)
        path.append(cells[left_ptr])
        left_ptr += 1

        # If there are still cells remaining, pick the cell with the largest coordinates
        # (from the right pointer)
        if left_ptr <= right_ptr:
            path.append(cells[right_ptr])
            right_ptr -= 1
            
    return path

```