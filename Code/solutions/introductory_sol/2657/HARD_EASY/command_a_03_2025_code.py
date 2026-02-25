```python
def first_chars(s: str) -> str:
    """
    Returns a new string with the first character of each word in the input string.

    Args:
        s (str): The input string containing words separated by spaces.

    Returns:
        str: A new string containing the first character of each word.
    """
    return ''.join(word[0] for word in s.split())
```