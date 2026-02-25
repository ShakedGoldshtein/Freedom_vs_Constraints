```python
def solve(n: int) -> str:
    """
    Returns the nth Fibonacci string.

    The Fibonacci string sequence is defined as:
    f0 = '0'
    f1 = '01'
    f2 = '010' = f1 + f0
    f3 = '01001' = f2 + f1
    and so on.

    Args:
        n (int): The index of the Fibonacci string to return.

    Returns:
        str: The nth Fibonacci string.
    """
    if n == 0:
        return '0'
    elif n == 1:
        return '01'

    # Initialize the first two Fibonacci strings
    a, b = '0', '01'

    # Generate the nth Fibonacci string
    for _ in range(2, n + 1):
        # Compute the next Fibonacci string by concatenating the previous two
        a, b = b, b + a

    return b
```