```python
def solve(n: int) -> str:
    """
    Adds a dot (.) as the thousands separator to the given integer and returns it as a string.

    Args:
        n (int): The integer to format.

    Returns:
        str: The formatted string with dots as thousands separators.
    """
    if n < 1000:
        return str(n)  # No need to add separators for numbers less than 1000

    result: list[str] = []
    num_str: str = str(n)
    length: int = len(num_str)

    # Iterate over the digits from right to left
    for i in range(length):
        # Add the current digit to the result
        result.insert(0, num_str[length - 1 - i])
        # Add a dot after every third digit (except the last group)
        if (i + 1) % 3 == 0 and i != length - 1:
            result.insert(0, ".")

    return "".join(result)
```