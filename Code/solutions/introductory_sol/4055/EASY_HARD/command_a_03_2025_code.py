```python
def solve(n: int) -> str:
    """
    Returns the nth Fibonacci string.

    The Fibonacci string sequence is defined as:
    f0 = '0'
    f1 = '01'
    fn = fn-1 + fn-2 for n > 1

    Args:
        n (int): The index of the Fibonacci string to return.

    Returns:
        str: The nth Fibonacci string.
    """
    # Base cases: return the initial strings for n = 0 and n = 1
    if n == 0:
        return "0"
    if n == 1:
        return "01"

    # Initialize the first two Fibonacci strings
    a, b = "0", "01"

    # Iterate from 2 to n to compute the nth Fibonacci string
    for _ in range(2, n + 1):
        # Update a and b to the last two Fibonacci strings
        a, b = b, b + a

    return b
```