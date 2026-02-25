```python
def solve(n, x):
    """
    Generates a grid configuration of rocks and an initial activation point
    to produce at least 'x' sounds.

    The strategy uses a simple rock arrangement that guarantees movement and sound
    production, often in a repeating cycle, to meet the 'x' sound requirement.

    Args:
        n (int): The size of the n x n grid.
        x (int): The minimum number of sounds required.

    Returns:
        tuple: A tuple containing:
            - list[str]: A list of strings representing the n x n grid.
            - tuple[int, int]: A 1-indexed (row, column) tuple for the
                               initial activated rock.
    """
    grid = [['.' for _ in range(n)] for _ in range(n)]
    
    start_row, start_col = 1, 1  # Default initial activation at (1,1)

    if n == 1:
        # For n=1, only one cell. Place '>' and it hits the wall.
        # Produces 1 sound. 'x' must be 1 in this case.
        grid[0][0] = '>'
        start_row, start_col = 1, 1
    elif n == 2:
        # For n=2, we can use '>v' arrangement.
        #   > v
        #   . .
        # 1. Activate (1,1) '>'. It moves right, hits 'v' at (1,2). 1 sound. 'v' activates.
        # 2. 'v' at (1,2) moves down, hits the wall. 1 sound. Movement ends.
        # This produces a total of 2 sounds, satisfying x=1 or x=2.
        grid[0][0] = '>'
        grid[0][1] = 'v'
        start_row, start_col = 1, 1
    else:  # n >= 3
        # For n >= 3, we can create a self-sustaining cycle that produces sounds indefinitely.
        #   > . < . . ...
        #   . . . . . ...
        #   . . . . . ...
        # 1. Activate (1,1) '>'. It moves right, through (1,2), hits '<' at (1,3). 1 sound. '<' activates.
        # 2. '<' at (1,3) moves left, through (1,2), hits '>' at (1,1). 1 sound. '>' activates.
        # This cycle produces 2 sounds every 2 activations, generating more than enough sounds
        # within the 10^7 event limit.
        grid[0][0] = '>'
        grid[0][2] = '<'
        start_row, start_col = 1, 1
    
    # Convert the list of lists (grid) into a list of strings for the output format.
    result_grid = ["".join(row) for row in grid]
    
    return result_grid, (start_row, start_col)
```