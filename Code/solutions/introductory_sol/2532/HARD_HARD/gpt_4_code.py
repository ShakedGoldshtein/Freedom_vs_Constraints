```python
def format_number(n: int) -> str:
    """Accepts an integer and formats it as a string with dots as thousands separators."""
    # Convert to string and reverse
    s = str(n)[::-1]
    chunks, chunk_size = len(s), 3
    # Create chunks of maximum size 3 and joint them with "."
    s = '.'.join(s[i:i+chunk_size] for i in range(0, chunks, chunk_size))
    # Return reversed result to maintain original order
    return s[::-1]
```