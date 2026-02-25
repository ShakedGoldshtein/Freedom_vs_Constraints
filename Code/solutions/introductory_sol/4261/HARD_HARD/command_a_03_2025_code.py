```python
def robot_walk(a: list[int]) -> bool:
    """
    Determines if there is a square that the robot visits at least twice after executing all commands.

    Args:
        a (list[int]): An array of positive integers, each representing a command.

    Returns:
        bool: True if there is a square visited at least twice, False otherwise.
    """
    # Initialize the robot's position and direction
    x, y = 0, 0
    direction = 0  # 0: North, 1: East, 2: South, 3: West
    visited = {(x, y)}  # Set to keep track of visited positions

    # Define the possible movements based on direction
    movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for step in a:
        for _ in range(step):
            # Move the robot one step in the current direction
            dx, dy = movements[direction]
            x += dx
            y += dy
            # Check if the new position has been visited before
            if (x, y) in visited:
                return True
            visited.add((x, y))
        # Turn 90 degrees clockwise after completing the step
        direction = (direction + 1) % 4

    return False
```