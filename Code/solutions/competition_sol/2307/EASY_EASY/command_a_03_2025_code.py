```python
def solve(N: int, A: int, B: int, X: list[int]) -> int:
    """
    Calculate the minimum possible total increase of fatigue level when visiting all towns.

    Args:
        N (int): Number of towns.
        A (int): Fatigue increase per unit distance walked.
        B (int): Fatigue increase per teleportation.
        X (list[int]): List of town coordinates.

    Returns:
        int: Minimum total fatigue level increase.
    """
    total_fatigue = 0
    for i in range(N - 1):
        # Calculate the distance between consecutive towns
        distance = X[i + 1] - X[i]
        # Decide whether to walk or teleport based on cost comparison
        if A * distance < B:
            # Walking is cheaper, add walking fatigue
            total_fatigue += A * distance
        else:
            # Teleporting is cheaper, add teleportation fatigue
            total_fatigue += B
    return total_fatigue
```