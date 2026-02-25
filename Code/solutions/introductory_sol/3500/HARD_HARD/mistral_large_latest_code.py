```python
def remove_exclamation_marks(s: str) -> str:
    """
    Removes all exclamation marks from the input string.

    Args:
        s: Input string potentially containing exclamation marks.

    Returns:
        A new string with all exclamation marks removed.

    Examples:
        >>> remove_exclamation_marks("Hello World!")
        "Hello World"
        >>> remove_exclamation_marks("!!!Hi!!!")
        "Hi"
        >>> remove_exclamation_marks("")
        ""
    """
    return s.replace('!', '')
```