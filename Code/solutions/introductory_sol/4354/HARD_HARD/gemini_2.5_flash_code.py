```python
class PadovanSequenceError(ValueError):
    """Custom exception for errors related to Padovan sequence calculations."""
    pass

def padovan(n: int) -> int:
    """
    Calculates the n-th Padovan number.

    The Padovan sequence P(n) is defined by the initial values:
    P(0) = 1
    P(1) = 1
    P(2) = 1
    and the recurrence relation:
    P(n) = P(n-2) + P(n-3) for n >= 3.

    This function uses an iterative approach with O(1) space complexity
    and O(n) time complexity, which is optimal.

    Args:
        n: The index of the Padovan number to calculate (non-negative integer).

    Returns:
        The n-th Padovan number.

    Raises:
        TypeError: If n is not an integer type.
        PadovanSequenceError: If n is a negative integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")

    if n < 0:
        raise PadovanSequenceError("Input 'n' must be a non-negative integer.")

    # Base cases: P(0) = 1, P(1) = 1, P(2) = 1
    if n <= 2:
        return 1

    # Iterative approach using O(1) space.
    # We maintain the last three required Padovan numbers to calculate the next one.
    # p_prev_3 corresponds to P(i-3)
    # p_prev_2 corresponds to P(i-2)
    # p_prev_1 corresponds to P(i-1)
    p_prev_3 = 1  # P(0)
    p_prev_2 = 1  # P(1)
    p_prev_1 = 1  # P(2)

    # Calculate P(i) for i from 3 up to n
    for _ in range(3, n + 1):
        current_padovan = p_prev_3 + p_prev_2
        
        # Shift values for the next iteration:
        # P(i-3) becomes P(i-2)
        # P(i-2) becomes P(i-1)
        # P(i-1) becomes P(i) (current_padovan)
        p_prev_3 = p_prev_2
        p_prev_2 = p_prev_1
        p_prev_1 = current_padovan
        
    return p_prev_1
```