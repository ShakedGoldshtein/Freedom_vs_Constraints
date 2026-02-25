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

    # Iterate through the array to check monotonicity
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            increasing = False
        if A[i] < A[i + 1]:
            decreasing = False

    # The array is monotonic if it is either increasing or decreasing
    return increasing or decreasing
```