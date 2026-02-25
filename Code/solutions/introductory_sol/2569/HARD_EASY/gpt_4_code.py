```python
def capitalize_name(full_name):
    """
    Function to capitalize the first and last names of a person
    """
    if not 0 < len(full_name) < 1000:
        return "Invalid input length"
        
    if not all(c.isalnum() or c.isspace() for c in full_name):
        return "Invalid characters in the input"

    return ' '.join(word.capitalize() for word in full_name.split())
```