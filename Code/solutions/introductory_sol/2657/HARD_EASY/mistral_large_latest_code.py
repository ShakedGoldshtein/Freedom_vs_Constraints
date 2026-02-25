```python
def get_first_letters(s: str) -> str:
    """
    Extracts the first character of each word in a string and returns them concatenated.

    Args:
        s: Input string containing words separated by whitespace.

    Returns:
        A string composed of the first character of each word in the input string.
        Returns an empty string if the input is empty or contains no words.

    Examples:
        >>> get_first_letters("This Is A Test")
        'TIAT'
        >>> get_first_letters("")
        ''
        >>> get_first_letters("   ")
        ''
        >>> get_first_letters("Hello   World  ")
        'HW'
    """
    if not s.strip():
        return ""

    words = s.split()
    return "".join(word[0] for word in words if word)
```