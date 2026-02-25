```python
def padovan(n: int) -> int:
    """
    Compute the nth Padovan number using an efficient iterative approach.

    Args:
        n: A non-negative integer representing the index in the Padovan sequence.

    Returns:
        The nth Padovan number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n <= 2:
        return 1

    a, b, c = 1, 1, 1  # P(0), P(1), P(2)
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b

    return c
```