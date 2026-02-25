```python
def solve(n: int) -> str:
    """
    Returns the nth Fibonacci string defined by the recurrence:
    f0 = '0'
    f1 = '01'
    fn = f(n-1) + f(n-2) for n >= 2

    Args:
        n: A non-negative integer representing the index of the Fibonacci string.

    Returns:
        The nth Fibonacci string.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n == 0:
        return '0'
    if n == 1:
        return '01'

    prev_prev = '0'  # f0
    prev = '01'      # f1

    for _ in range(2, n + 1):
        current = prev + prev_prev
        prev_prev, prev = prev, current

    return prev
```