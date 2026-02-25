```python
def is_monotonic(A: list) -> bool:
    """
    Checks if an array is monotonic (either monotone increasing or monotone decreasing).

    An array is monotone increasing if for all i <= j, A[i] <= A[j].
    An array is monotone decreasing if for all i <= j, A[i] >= A[j].

    Args:
        A: A list of integers. Constraints: 1 <= A.length <= 50000, -100000 <= A[i] <= 100000.

    Returns:
        True if the array A is monotonic, False otherwise.
    """
    n = len(A)

    # An array with 0 or 1 elements is inherently monotonic.
    # The problem constraints state 1 <= A.length, so n >= 1.
    # Any array with 2 elements is also monotonic (e.g., [1,2], [2,1], [1,1]).
    if n <= 2:
        return True

    is_increasing = True
    is_decreasing = True

    # Iterate through the array starting from the second element
    # to compare each element with its predecessor.
    for i in range(1, n):
        # If the current element is greater than the previous, it cannot be decreasing.
        if A[i] > A[i-1]:
            is_decreasing = False
        # If the current element is less than the previous, it cannot be increasing.
        elif A[i] < A[i-1]:
            is_increasing = False
        
        # Optimization: If both flags become False,
        # it means the array is neither purely increasing nor purely decreasing.
        # We can stop early and return False.
        if not is_increasing and not is_decreasing:
            return False

    # The array is monotonic if it was found to be purely increasing
    # OR purely decreasing (or both, which happens for arrays with all same elements).
    return is_increasing or is_decreasing
```