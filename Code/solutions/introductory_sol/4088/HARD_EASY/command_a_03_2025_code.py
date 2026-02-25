```python
def tetris(gamelog: list[str]) -> int:
    """
    Simulates a Tetris game based on the given gamelog and returns the number of cleared lines.

    Args:
        gamelog (list[str]): A list of commands representing the game log.
                             Each command is a string in the format 'type direction offset'.

    Returns:
        int: The total number of cleared lines.
    """

    # Initialize the game field as a list of lists, representing a 30x9 grid.
    # Each cell is initially 0, representing an empty space.
    field: list[list[int]] = [[0] * 9 for _ in range(30)]
    cleared_lines: int = 0  # Counter for the number of cleared lines

    # Define the block shapes based on their type (1 to 4).
    # Each block is represented as a list of tuples (row_offset, col_offset).
    blocks: list[list[tuple[int, int]]] = [
        [(0, 0)],  # Block type 1: single cell
        [(0, 0), (0, 1)],  # Block type 2: two cells horizontally
        [(0, 0), (0, 1), (0, 2)],  # Block type 3: three cells horizontally
        [(0, 0), (0, 1), (0, 2), (0, 3)],  # Block type 4: four cells horizontally
    ]

    # Mapping from direction and offset to the corresponding column index.
    # L4 to R4 maps to columns 0 to 8, respectively.
    direction_offset_to_col: dict[str, dict[int, int]] = {
        "L": {4: 0, 3: 1, 2: 2, 1: 3, 0: 4},
        "R": {4: 8, 3: 7, 2: 6, 1: 5, 0: 4},
    }

    for command in gamelog:
        block_type: int = int(command[0])  # Extract block type from command
        direction: str = command[1]  # Extract direction from command
        offset: int = int(command[2])  # Extract offset from command

        # Calculate the starting column based on direction and offset
        start_col: int = direction_offset_to_col[direction][offset]

        # Check if the block can be placed without exceeding the field height
        for row_offset, col_offset in blocks[block_type - 1]:
            row: int = 0  # Start from the top row
            col: int = start_col + col_offset  # Calculate the column for the current cell

            # Move the block down as far as possible
            while row + row_offset < 30 and not field[row + row_offset][col]:
                row += 1

            # If the block cannot be placed at the bottom, the game ends
            if row + row_offset >= 30:
                return cleared_lines

            # Place the block in the field
            field[row + row_offset][col] = 1

        # Check for and clear any full lines
        for row in range(30):
            if all(field[row]):  # If all cells in the row are filled
                cleared_lines += 1  # Increment the cleared lines counter
                # Shift all rows above the cleared row down by one
                for r in range(row, 0, -1):
                    field[r] = field[r - 1].copy()
                # Clear the top row
                field[0] = [0] * 9

    return cleared_lines
```