```python
def more_zeros(s: str) -> list[str]:
    """
    Returns a list of characters from the input string whose binary representation
    of ASCII value contains more zeros than ones, removing duplicates and preserving order.

    Args:
        s (str): The input string to process.

    Returns:
        list[str]: A list of characters meeting the criteria, in order of first occurrence.
    """
    seen = set()  # To track characters already added to the result
    result = []

    for char in s:
        # Check if the character has already been added to the result
        if char in seen:
            continue

        # Count zeros and ones in the binary representation of the ASCII value
        binary = bin(ord(char))[2:]  # Get binary representation without '0b' prefix
        zeros = binary.count('0')
        ones = binary.count('1')

        # Check if zeros are more than ones
        if zeros > ones:
            result.append(char)
            seen.add(char)  # Mark the character as seen

    return result
```