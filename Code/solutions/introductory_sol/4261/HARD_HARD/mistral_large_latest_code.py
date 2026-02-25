```python
def has_duplicate_visits(commands):
    """
    Determines if the robot visits any square at least twice after executing all commands.

    Args:
        commands: List[int], a list of positive integers representing movement commands.

    Returns:
        bool: True if any square is visited at least twice, False otherwise.
    """
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W
    x, y = 0, 0
    visited = {(0, 0)}
    current_dir = 0  # Start facing north (0th direction)

    for cmd in commands:
        dx, dy = directions[current_dir]
        for _ in range(cmd):
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            visited.add((x, y))
        current_dir = (current_dir + 1) % 4  # Turn 90° clockwise

    return False
```