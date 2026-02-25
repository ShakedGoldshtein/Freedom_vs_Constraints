```python
def decimal_to_factorial(n: int) -> str:
    """Convert a decimal number to its factorial representation.

    Args:
        n: A positive integer to convert.

    Returns:
        The factorial representation as a string using digits 0-9 and letters A-Z.
    """
    if n < 0:
        raise ValueError("Input must be a positive integer")

    digits = []
    base = 1
    factor = 1

    while True:
        if n < factor:
            digits.append(0)
            break
        digit = n // factor
        if digit >= factor:
            raise ValueError("Invalid input: digit exceeds base")
        digits.append(digit)
        n %= factor
        factor += 1

    # Remove trailing zeros (except the last one)
    while len(digits) > 1 and digits[-2] == 0:
        digits.pop()

    # Convert digits to characters (0-9, A-Z)
    char_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(char_map[d] for d in reversed(digits))

def factorial_to_decimal(s: str) -> int:
    """Convert a factorial representation string back to a decimal number.

    Args:
        s: A string representing a number in factorial notation using digits 0-9 and letters A-Z.

    Returns:
        The decimal representation as an integer.
    """
    if not s:
        raise ValueError("Input string cannot be empty")

    char_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    max_digit = len(char_map) - 1

    digits = []
    for c in reversed(s.upper()):
        if c not in char_map:
            raise ValueError(f"Invalid character '{c}' in input")
        digit = char_map.index(c)
        if digit > len(digits):
            raise ValueError(f"Digit {digit} exceeds position {len(digits)}")
        digits.append(digit)

    result = 0
    factorial = 1
    for i, d in enumerate(digits):
        if d < 0 or d > i:
            raise ValueError(f"Digit {d} at position {i} is invalid")
        result += d * factorial
        factorial *= (i + 1)

    return result
```