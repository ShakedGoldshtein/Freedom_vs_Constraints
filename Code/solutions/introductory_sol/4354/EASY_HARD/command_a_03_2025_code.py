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
    """
    if n < 3:
        return 1
    a, b, c = 1, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b
    return c
```