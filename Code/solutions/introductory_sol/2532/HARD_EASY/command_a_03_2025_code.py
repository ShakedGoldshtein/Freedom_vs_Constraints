```python
def format_with_thousands_separator(n: int) -> str:
    """
    Formats an integer with dots as thousands separators.

    Args:
        n (int): The integer to format.

    Returns:
        str: The formatted string with dots as thousands separators.
    """
    if n == 0:
        return "0"

    result: list[str] = []
    num_str: str = str(n)
    length: int = len(num_str)

    for i, char in enumerate(reversed(num_str)):
        result.append(char)
        if (i + 1) % 3 == 0 and i != length - 1:
            result.append(".")

    return "".join(reversed(result))
```