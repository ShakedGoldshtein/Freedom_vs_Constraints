```python
def tetris(gamelog: list[str]) -> int:
    """
    Simulates a simplified Tetris game based on the given game log and returns the number of cleared lines.

    Args:
        gamelog (list[str]): A list of commands representing the game log. Each command is a string in the format 'type direction offset'.

    Returns:
        int: The total number of cleared lines.
    """
    # Initialize the game field as a list of lists, representing a 30x9 grid.
    # Each row is initialized with zeros, representing empty spaces.
    field: list[list[int]] = [[0] * 9 for _ in range(30)]
    cleared_lines: int = 0  # Counter for the number of cleared lines

    for command in gamelog:
        block_type: int = int(command[0])  # Extract block type from the command
        direction: str = command[1]  # Extract direction from the command
        offset: int = int(command[2])  # Extract offset from the command

        # Calculate the starting position based on the direction and offset.
        # The center of the field is at index 4, so adjust accordingly.
        start_pos: int = 4 - offset if direction == "L" else 4 + offset

        # Check if the block can be placed without exceeding the field height.
        # If the block type is 1, it occupies only one row, so check the first row.
        # For other block types, check the corresponding number of rows.
        if block_type == 1 and any(field[i][start_pos] for i in range(block_type)):
            break  # Game ends if the block cannot be placed
        elif block_type > 1 and any(
            field[i][start_pos : start_pos + block_type] for i in range(block_type)
        ):
            break  # Game ends if the block cannot be placed

        # Place the block on the field.
        # For each row that the block occupies, mark the corresponding positions as filled (1).
        for i in range(block_type):
            for j in range(block_type):
                field[i][start_pos + j] = 1

        # Check for and clear any full lines.
        # Iterate over each row in the field.
        for i in range(30):
            if all(field[i]):  # If all positions in the row are filled (1)...
                cleared_lines += 1  # Increment the cleared lines counter
                # Shift all rows above the cleared row down by one position.
                for j in range(i, 0, -1):
                    field[j] = field[j - 1].copy()
                # Reset the top row to all zeros (empty spaces).
                field[0] = [0] * 9

    return cleared_lines
```