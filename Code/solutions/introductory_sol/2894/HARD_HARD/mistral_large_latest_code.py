```python
def triple_trouble(str1: str, str2: str, str3: str) -> str:
    """
    Combines three input strings by interleaving their characters in groups.

    Args:
        str1: First input string.
        str2: Second input string.
        str3: Third input string.

    Returns:
        A new string formed by taking the first character of each input string,
        followed by the second character of each, and so on.

    Raises:
        ValueError: If input strings have unequal lengths.
    """
    if not (len(str1) == len(str2) == len(str3)):
        raise ValueError("All input strings must have the same length")

    return ''.join(
        char1 + char2 + char3
        for char1, char2, char3 in zip(str1, str2, str3)
    )
```