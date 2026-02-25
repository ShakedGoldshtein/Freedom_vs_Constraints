```python
def format_with_thousands_separator(n: int) -> str:
    """
    Formats an integer with dots as thousands separators.

    Args:
        n: Non-negative integer to format (0 <= n < 2^31).

    Returns:
        String representation of the number with dots as thousands separators.
    """
    if n == 0:
        return "0"

    is_negative = n < 0
    n = abs(n)

    parts = []
    while n > 0:
        parts.append(f"{n % 1000:03d}")
        n = n // 1000

    # Remove leading zeros from the most significant part
    if parts:
        parts[-1] = str(int(parts[-1]))

    formatted = ".".join(reversed(parts))

    return f"-{formatted}" if is_negative else formatted
```