```python
def format_number(n):
    """
    Format an integer with thousands separators.
    
    Args:
        n: Integer to format (0 <= n < 2^31)
    
    Returns:
        String representation of n with '.' as thousands separator
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    if n >= 2**31:
        raise ValueError("Input must be less than 2^31")
    
    if n == 0:
        return "0"
    
    result = []
    str_n = str(n)
    length = len(str_n)
    
    # Calculate where the first group starts
    first_group_length = length % 3
    if first_group_length == 0:
        first_group_length = 3
    
    # Add first group
    if first_group_length > 0:
        result.append(str_n[:first_group_length])
    
    # Process remaining groups of 3 digits
    for i in range(first_group_length, length, 3):
        result.append(str_n[i:i+3])
    
    return '.'.join(result)

def thousands_separator(n):
    """
    Add a dot (".") as the thousands separator to an integer.
    
    Args:
        n: Integer to format
        
    Returns:
        String with thousands separated by dots
    """
    return format_number(n)
```