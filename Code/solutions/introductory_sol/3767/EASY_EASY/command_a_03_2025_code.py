```python
from math import factorial

# Mapping for digits to characters (0-9, A-Z)
DIGITS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def dec2FactString(n: int) -> str:
    """
    Convert a decimal number to its factorial representation as a string.
    
    Args:
        n (int): The decimal number to convert.
    
    Returns:
        str: The factorial representation of the number as a string.
    """
    if n == 0:
        return '0'
    
    result: list[str] = []
    i: int = 2
    while n > 0:
        # Calculate the remainder when divided by i!
        remainder: int = n % i
        # Append the corresponding digit to the result
        result.append(DIGITS[remainder])
        # Subtract the remainder and divide by i to move to the next factorial base
        n = (n - remainder) // i
        i += 1
    
    # Reverse the result to get the correct order and join into a string
    return ''.join(reversed(result))

def factString2Dec(s: str) -> int:
    """
    Convert a factorial representation string to its decimal equivalent.
    
    Args:
        s (str): The factorial representation string to convert.
    
    Returns:
        int: The decimal equivalent of the factorial representation.
    """
    if s == '0':
        return 0
    
    result: int = 0
    # Iterate over the string from right to left (starting from the least significant digit)
    for i, char in enumerate(reversed(s), start=1):
        # Get the numerical value of the character (0-35)
        digit: int = DIGITS.index(char)
        # Add the value to the result, scaled by the factorial of the current position
        result += digit * factorial(i)
    
    return result
```