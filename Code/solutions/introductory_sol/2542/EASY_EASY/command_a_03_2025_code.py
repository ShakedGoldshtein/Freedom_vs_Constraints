```python
def isMonotonic(A: list[int]) -> bool:
    """
    Determines if the given array is monotonic (either monotone increasing or decreasing).

    Args:
        A (list[int]): The input array to check for monotonicity.

    Returns:
        bool: True if the array is monotonic, False otherwise.
    """
    increasing = decreasing = True

    # Iterate through the array to check for monotonicity
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            increasing = False  # Found a decrease, not increasing
        if A[i] < A[i + 1]:
            decreasing = False  # Found an increase, not decreasing
        if not increasing and not decreasing:
            return False  # Array is neither increasing nor decreasing

    return True
```