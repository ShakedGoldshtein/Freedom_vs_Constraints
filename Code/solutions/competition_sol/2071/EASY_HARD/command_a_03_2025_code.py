```python
def solve(n: int, points: list[tuple[int, int]]) -> int:
    """
    Calculate the number of pairs of watchmen where the Manhattan distance equals the Euclidean distance.

    Args:
        n (int): The number of watchmen.
        points (list of tuples): A list of tuples where each tuple contains the coordinates (x, y) of a watchman.

    Returns:
        int: The number of pairs where the Manhattan distance equals the Euclidean distance.
    """
    # Create a dictionary to count occurrences of each point
    point_counts: dict[tuple[int, int], int] = {}
    for x, y in points:
        point_counts[(x, y)] = point_counts.get((x, y), 0) + 1

    # Initialize the result with the sum of combinations of points with the same coordinates
    result: int = 0
    for count in point_counts.values():
        if count >= 2:
            # Calculate the number of pairs for points with the same coordinates
            result += count * (count - 1) // 2

    # Create dictionaries to count occurrences of each x and y coordinate
    x_counts: dict[int, int] = {}
    y_counts: dict[int, int] = {}
    for x, y in points:
        x_counts[x] = x_counts.get(x, 0) + 1
        y_counts[y] = y_counts.get(y, 0) + 1

    # Add the product of counts of x and y coordinates to the result
    for count in x_counts.values():
        result += count * (count - 1) // 2
    for count in y_counts.values():
        result += count * (count - 1) // 2

    # Subtract the counts of points with the same coordinates to avoid double counting
    for count in point_counts.values():
        if count >= 2:
            result -= count * (count - 1) // 2

    return result
```