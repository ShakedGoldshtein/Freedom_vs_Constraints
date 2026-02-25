```python
def disarium_number(n: int) -> str:
    """
    Determines if a given positive integer is a Disarium number.

    A Disarium number is a number where the sum of its digits each raised to the power
    of their respective positions (1-based index) equals the number itself.

    Args:
        n: A positive integer to check.

    Returns:
        "Disarium !!" if the number is Disarium, otherwise "Not !!".

    Examples:
        >>> disarium_number(89)
        "Disarium !!"
        >>> disarium_number(564)
        "Not !!"
    """
    digits = _extract_digits(n)
    return "Disarium !!" if _is_disarium(n, digits) else "Not !!"

def _extract_digits(n: int) -> list[int]:
    """Extracts digits of a number in reverse order (LSB first)."""
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    return digits[::-1]

def _is_disarium(n: int, digits: list[int]) -> bool:
    """Checks if the sum of digits^position equals the original number."""
    total = 0
    for position, digit in enumerate(digits, start=1):
        total += digit ** position
        if total > n:  # Early termination if sum exceeds n
            return False
    return total == n
```