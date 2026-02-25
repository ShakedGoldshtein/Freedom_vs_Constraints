```python
def is_palindrome(obj: str | int | float) -> bool:
    """
    Checks if the given object is a palindrome.

    Args:
        obj: Input to check. Can be a string, integer, or float.
             Floats are converted to strings without scientific notation.

    Returns:
        bool: True if the object is a palindrome, False otherwise.

    Raises:
        TypeError: If the input type is not string, int, or float.
    """
    if not isinstance(obj, (str, int, float)):
        raise TypeError("Input must be a string, integer, or float")

    # Convert to string representation (handles numbers, including floats)
    s = _to_string(obj)
    return _is_palindrome_sequence(s)

def _to_string(obj: str | int | float) -> str:
    """
    Converts the input object to a string representation suitable for palindrome checking.
    For floats, ensures no scientific notation is used.
    """
    if isinstance(obj, float):
        # Convert float to string without scientific notation
        return format(obj, '.15f').rstrip('0').rstrip('.') if '.' in format(obj, '.15f') else str(int(obj))
    return str(obj)

def _is_palindrome_sequence(s: str) -> bool:
    """
    Checks if the given string sequence is a palindrome.
    Considers all characters, including spaces, punctuation, and case.
    """
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True
```