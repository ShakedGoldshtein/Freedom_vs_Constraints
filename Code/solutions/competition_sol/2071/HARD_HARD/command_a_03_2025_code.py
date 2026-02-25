```python
from collections import defaultdict


def solve(n: int, points: list[tuple[int, int]]) -> int:
    """
    Calculate the number of pairs of watchmen where the Manhattan distance equals the Euclidean distance.

    Args:
        n (int): The number of watchmen.
        points (list of tuples): A list of (x, y) coordinates for each watchman.

    Returns:
        int: The number of pairs where the Manhattan distance equals the Euclidean distance.
    """
    # Count occurrences of each point to handle duplicates
    point_counts = defaultdict(int)
    for x, y in points:
        point_counts[(x, y)] += 1

    # Count occurrences of each x and y coordinate
    x_counts = defaultdict(int)
    y_counts = defaultdict(int)
    for (x, y), count in point_counts.items():
        x_counts[x] += count
        y_counts[y] += count

    # Calculate the total number of pairs where x coordinates are the same
    same_x = 0
    for count in x_counts.values():
        same_x += count * (count - 1) // 2

    # Calculate the total number of pairs where y coordinates are the same
    same_y = 0
    for count in y_counts.values():
        same_y += count * (count - 1) // 2

    # Calculate the number of pairs where both x and y coordinates are the same
    same_xy = 0
    for count in point_counts.values():
        same_xy += count * (count - 1) // 2

    # The result is the total number of pairs with the same x or y, minus the pairs counted twice
    return same_x + same_y - same_xy
```