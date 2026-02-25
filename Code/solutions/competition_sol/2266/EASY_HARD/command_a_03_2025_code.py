```python
def solve(N: int, M: int, LR: list[tuple[int, int]]) -> int:
    """
    Calculate the minimum number of additional chairs required.

    Args:
        N (int): Number of people.
        M (int): Number of chairs.
        LR (list of tuples): List of tuples where each tuple contains (L_i, R_i) for each person.

    Returns:
        int: The minimum number of additional chairs required.
    """
    # Sort the intervals based on R_i in ascending order
    LR.sort(key=lambda x: x[1])

    # Initialize the end of the last assigned chair
    last_chair = -1
    additional_chairs = 0

    for l, r in LR:
        # If the current interval starts after the last assigned chair, assign a chair within [l, r]
        if l > last_chair:
            last_chair = r
        # If the current interval overlaps with the last assigned chair, increment the additional chairs count
        else:
            additional_chairs += 1

    # The minimum number of additional chairs is the number of overlapping intervals
    return additional_chairs
```