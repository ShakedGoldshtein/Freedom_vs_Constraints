```python
def is_monotonic(arr):
    """
    Determines if the given array is monotonic (either entirely non-increasing or non-decreasing).

    Args:
        arr: List[int] - The input array to check for monotonicity.

    Returns:
        bool: True if the array is monotonic, False otherwise.
    """
    if not arr:
        return True

    is_increasing = True
    is_decreasing = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_increasing = False
        if arr[i] < arr[i + 1]:
            is_decreasing = False

        if not is_increasing and not is_decreasing:
            return False

    return True
```