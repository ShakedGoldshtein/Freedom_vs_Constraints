```python
def padovan(n: int) -> int:
    """
    Returns the nth Padovan number.

    The Padovan sequence is defined by:
    P(0) = P(1) = P(2) = 1
    P(n) = P(n-2) + P(n-3) for n > 2

    Args:
        n (int): The index of the Padovan number to compute.

    Returns:
        int: The nth Padovan number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Base cases
    if n <= 2:
        return 1
    
    # Initialize the first three Padovan numbers
    a, b, c = 1, 1, 1
    
    # Compute the nth Padovan number iteratively
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b
    
    return c
```