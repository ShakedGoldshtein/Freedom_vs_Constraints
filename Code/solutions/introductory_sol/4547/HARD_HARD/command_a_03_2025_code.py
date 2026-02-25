```python
def more_zeros(s: str) -> list[str]:
    """
    Returns a list of characters from the input string whose binary representation
    of ASCII value has more zeros than ones, removing duplicates and preserving order.

    Args:
        s (str): Input string of length > 0.

    Returns:
        list[str]: List of characters meeting the criteria, in order of first occurrence.
    """
    seen = set()  # Track seen characters to avoid duplicates
    result = []

    for char in s:
        if char not in seen:
            ascii_val = ord(char)
            binary = bin(ascii_val)[2:]  # Remove '0b' prefix
            zeros = binary.count('0')
            ones = binary.count('1')

            if zeros > ones:
                result.append(char)
                seen.add(char)

    return result
```