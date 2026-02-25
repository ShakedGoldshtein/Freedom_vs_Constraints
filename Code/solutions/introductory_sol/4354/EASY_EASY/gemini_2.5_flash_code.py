```python
def padovan(n: int) -> int:
    """
    Calculates the n-th Padovan number using an iterative approach with O(1) space complexity.

    The Padovan sequence is defined by:
    P(0) = 1
    P(1) = 1
    P(2) = 1
    P(n) = P(n-2) + P(n-3) for n > 2

    Args:
        n: The index of the Padovan number to calculate (non-negative integer).

    Returns:
        The n-th Padovan number.
    """
    if n == 0 or n == 1 or n == 2:
        return 1

    # Initialize variables to hold P(i-3), P(i-2), P(i-1)
    # These correspond to P(0), P(1), P(2) initially.
    p_n_minus_3 = 1  # Represents P(i-3)
    p_n_minus_2 = 1  # Represents P(i-2)
    p_n_minus_1 = 1  # Represents P(i-1)

    # Iterate from i = 3 up to n to calculate P(n)
    for _ in range(3, n + 1):
        # Calculate P(i) using the recurrence relation
        current_p = p_n_minus_2 + p_n_minus_3
        
        # Shift values for the next iteration:
        # P(i-3) becomes old P(i-2)
        # P(i-2) becomes old P(i-1)
        # P(i-1) becomes current P(i)
        p_n_minus_3 = p_n_minus_2
        p_n_minus_2 = p_n_minus_1
        p_n_minus_1 = current_p
    
    # After the loop, p_n_minus_1 holds the value of P(n)
    return p_n_minus_1
```