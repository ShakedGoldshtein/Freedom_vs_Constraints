```python
def solve(n: int, m: int, lr: list[tuple[int, int]]) -> int:
    """
    Calculate the minimum number of additional chairs required.

    Args:
        n (int): Number of people.
        m (int): Number of chairs.
        lr (list of tuples): List of (L_i, R_i) pairs representing the preferred chair ranges for each person.

    Returns:
        int: Minimum number of additional chairs needed.
    """
    # Sort the intervals based on R_i to facilitate greedy assignment
    intervals = sorted([(l, r) for l, r in lr], key=lambda x: x[1])

    # Initialize the last assigned chair position
    last_assigned = -1
    additional_chairs = 0

    for l, r in intervals:
        # Find the earliest possible chair within the range [l, r] that is not already assigned
        # Since chairs are at integer positions, we can iterate through them
        for chair in range(int(l), int(r) + 1):
            if chair > last_assigned:
                last_assigned = chair
                break
        else:
            # If no chair is available within [l, r], an additional chair is needed
            additional_chairs += 1

    return additional_chairs
```