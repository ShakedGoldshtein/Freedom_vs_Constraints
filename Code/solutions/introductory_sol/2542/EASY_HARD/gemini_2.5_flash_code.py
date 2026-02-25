```python
def isMonotonic(A: list) -> bool:
    """
    Checks if the given array A is monotonic (either monotone increasing or monotone decreasing).

    An array A is monotone increasing if for all i <= j, A[i] <= A[j].
    An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

    Args:
        A: A list of integers.

    Returns:
        True if the array A is monotonic, False otherwise.
    """
    is_increasing = True
    is_decreasing = True

    # An array with 0 or 1 element is always monotonic.
    # The constraints guarantee 1 <= A.length, so we only need to consider A.length >= 1.
    # If len(A) == 1, the loop below won't execute, and it will correctly return True.

    for i in range(1, len(A)):
        if A[i] < A[i - 1]:
            is_increasing = False
        if A[i] > A[i - 1]:
            is_decreasing = False
        
        # Optimization: If both flags become False, we can short-circuit and return immediately.
        if not is_increasing and not is_decreasing:
            return False

    # The array is monotonic if it is either entirely increasing or entirely decreasing.
    return is_increasing or is_decreasing
```