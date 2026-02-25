```python
def encode(s: str) -> str:
    """
    Replaces all letters in the input string with their respective positions in the English alphabet.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string with letters replaced by their positions.
    """
    result: list[str] = []
    for char in s:
        if char.isalpha():
            # Calculate the position in the alphabet (1-based index)
            # ord('a') is 97, ord('A') is 65
            # Subtracting 96 for lowercase and 64 for uppercase gives the position
            position = ord(char.lower()) - 96
            result.append(str(position))
        else:
            result.append(char)
    return ''.join(result)
```