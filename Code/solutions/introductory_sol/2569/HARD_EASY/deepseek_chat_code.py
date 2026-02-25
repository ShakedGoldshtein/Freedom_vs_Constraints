```python
def capitalize_name(full_name):
    """
    Capitalize the first letter of each word in the given full name.
    
    Args:
        full_name (str): The input string containing the full name
        
    Returns:
        str: The capitalized name where each word starts with uppercase
    """
    if not full_name:
        return ""
    
    words = full_name.split(' ')
    capitalized_words = []
    
    for word in words:
        if word:
            capitalized_words.append(word[0].upper() + word[1:])
        else:
            capitalized_words.append('')
    
    return ' '.join(capitalized_words)
```