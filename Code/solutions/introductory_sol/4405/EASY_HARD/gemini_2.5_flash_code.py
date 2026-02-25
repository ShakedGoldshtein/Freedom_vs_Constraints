```python
def isPalindrome(obj):
    """
    Checks if an input (string or number) is a palindrome.
    A palindrome reads the same backward or forward, including capital letters,
    punctuation, and word dividers.

    Args:
        obj: The input to check, can be a string or an integer.

    Returns:
        bool: True if the input is a palindrome, False otherwise.
    """
    s = str(obj)
    return s == s[::-1]
```