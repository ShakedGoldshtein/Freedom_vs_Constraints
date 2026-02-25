```python
def is_palindrome(s: any) -> bool:
    """
    Checks if the input is a palindrome.

    Args:
    s (any): The input to check. Can be a string, integer, or any other type that can be converted to a string.

    Returns:
    bool: True if the input is a palindrome, False otherwise.
    """
    # Convert input to string, ignoring case and non-alphanumeric characters
    s = ''.join(filter(str.isalnum, str(s))).lower()
    
    # Compare the string with its reverse
    return s == s[::-1]
```