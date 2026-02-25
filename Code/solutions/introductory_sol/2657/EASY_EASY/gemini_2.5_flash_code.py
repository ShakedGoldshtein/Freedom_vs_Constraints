```python
def get_first_chars(input_string: str) -> str:
    """
    Returns a new string composed of the first character of each word in the input string.

    Args:
        input_string: The string to process.

    Returns:
        A new string with the first character of each word.
    """
    words = input_string.split()
    if not words:
        return ""
    
    first_chars = [word[0] for word in words]
    return "".join(first_chars)
```