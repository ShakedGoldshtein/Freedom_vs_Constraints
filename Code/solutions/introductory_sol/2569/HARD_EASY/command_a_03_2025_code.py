```python
def solve(full_name: str) -> str:
    """
    Capitalize the first and last names in a full name string.

    Args:
        full_name (str): The full name string to be capitalized.

    Returns:
        str: The capitalized full name string.
    """
    # Split the full name into individual words
    words = full_name.split()

    # Capitalize each word and join them back into a single string
    capitalized_name = " ".join(word.capitalize() for word in words)

    return capitalized_name
```