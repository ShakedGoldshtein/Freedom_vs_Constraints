```python
def is_palindrome(s):
    """
    Check if the input is a palindrome.
    
    Args:
        s: Input to check (can be string, number, or any type that can be converted to string)
    
    Returns:
        bool: True if the input is a palindrome, False otherwise
    """
    if s is None:
        return False
    
    try:
        str_representation = str(s)
    except (TypeError, ValueError):
        return False
    
    if not str_representation:
        return True
    
    left = 0
    right = len(str_representation) - 1
    
    while left < right:
        if str_representation[left] != str_representation[right]:
            return False
        left += 1
        right -= 1
    
    return True
```