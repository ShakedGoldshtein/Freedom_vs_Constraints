```python
def encode(s: str) -> str:
    """
    Encodes a string by replacing each alphabetic character with its 1-based position in the English alphabet.
    Non-alphabetic characters remain unchanged. The function is case-sensitive.

    Args:
        s: Input string to be encoded.

    Returns:
        Encoded string where alphabetic characters are replaced by their positions.
    """
    def _char_to_position(c: str) -> str:
        if 'a' <= c <= 'z':
            return str(ord(c) - ord('a') + 1)
        elif 'A' <= c <= 'Z':
            return str(ord(c) - ord('A') + 1)
        return c

    return ''.join(_char_to_position(c) for c in s)
```