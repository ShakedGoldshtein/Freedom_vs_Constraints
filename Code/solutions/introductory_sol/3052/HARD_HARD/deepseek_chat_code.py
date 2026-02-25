```python
def remove(s):
    """
    Remove all exclamation marks from the sentence except those at the end.
    
    Args:
        s (str): Input string that may contain exclamation marks
        
    Returns:
        str: String with all non-trailing exclamation marks removed
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    if not s:
        return s
    
    # Count trailing exclamation marks
    trailing_count = 0
    for char in reversed(s):
        if char == '!':
            trailing_count += 1
        else:
            break
    
    # Remove all exclamation marks from the non-trailing portion
    main_part = s[:-trailing_count] if trailing_count > 0 else s
    cleaned_main = main_part.replace('!', '')
    
    # Reconstruct the string with trailing exclamation marks
    return cleaned_main + ('!' * trailing_count)
```