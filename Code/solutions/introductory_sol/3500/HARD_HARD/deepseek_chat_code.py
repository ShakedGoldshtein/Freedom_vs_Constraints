```python
def remove_exclamation_marks(s: str) -> str:
    """
    Remove all exclamation marks from the input string.
    
    Args:
        s: Input string that may contain exclamation marks
        
    Returns:
        String with all exclamation marks removed
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    return s.replace('!', '')
```