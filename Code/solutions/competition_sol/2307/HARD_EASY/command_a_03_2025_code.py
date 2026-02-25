```python
def solve(n: int, a: int, b: int, x: list[int]) -> int:
    """
    Calculate the minimum possible total increase of fatigue level when visiting all towns.

    Args:
        n (int): Number of towns.
        a (int): Fatigue increase per unit distance walked.
        b (int): Fatigue increase per teleportation.
        x (list[int]): List of town coordinates in order from west to east.

    Returns:
        int: Minimum possible total fatigue increase.
    """
    total_fatigue = 0
    for i in range(n - 1):
        # Calculate the distance between consecutive towns
        distance = x[i + 1] - x[i]
        # Decide whether to walk or teleport based on cost comparison
        if a * distance > b:
            total_fatigue += b  # Teleport
        else:
            total_fatigue += a * distance  # Walk
    return total_fatigue
```