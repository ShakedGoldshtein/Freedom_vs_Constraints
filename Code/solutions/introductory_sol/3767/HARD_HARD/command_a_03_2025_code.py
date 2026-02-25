```python
from math import factorial

# Mapping for digits to characters (0-9, A-Z)
DIGITS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decimal_to_factorial(n: int) -> str:
    """
    Convert a decimal number to its factorial representation.

    Args:
        n (int): The decimal number to convert.

    Returns:
        str: The factorial representation of the number as a string.
    """
    if n == 0:
        return '0'

    result = []
    i = 1
    while n > 0:
        # Calculate the remainder when divided by i!
        remainder = n % i
        # Append the corresponding digit to the result
        result.append(DIGITS[remainder])
        # Subtract the remainder and divide by i to move to the next factorial base
        n = (n - remainder) // i
        i += 1

    # Reverse the result to get the correct order
    return ''.join(reversed(result))

def factorial_to_decimal(s: str) -> int:
    """
    Convert a factorial representation to a decimal number.

    Args:
        s (str): The factorial representation as a string.

    Returns:
        int: The decimal equivalent of the factorial representation.
    """
    if s == '0':
        return 0

    result = 0
    i = len(s) - 1
    for char in reversed(s):
        # Get the numerical value of the character
        digit = DIGITS.index(char)
        # Add the value multiplied by the corresponding factorial
        result += digit * factorial(i)
        i -= 1

    return result
```