```python
def format_thousands(n: int) -> str:
    """
    Given an integer n, add a dot (".") as the thousands separator and return it in string format.

    Args:
        n: The input integer.

    Returns:
        A string representation of the integer with dots as thousands separators.
    """
    s = str(n)
    parts = []
    k = len(s)

    # Extract groups of 3 digits from the right
    while k > 3:
        parts.append(s[k - 3:k])
        k -= 3
    
    # Add the remaining digits (the first group)
    parts.append(s[0:k])

    # Join the parts with a dot, in reverse order of extraction
    return ".".join(parts[::-1])
```