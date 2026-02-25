```python
def encode(s: str) -> str:
    """
    Replaces all letters in the input string with their respective positions in the English alphabet.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string with letters replaced by their positions.
    """
    return ''.join(str(ord(c) - 96) if c.islower() else c for c in s)
```