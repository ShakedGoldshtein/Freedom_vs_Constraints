```python
def solve(S: str) -> str:
    """
    Capitalizes the first and last names in a full name string.

    Args:
        S (str): The full name string to be capitalized.

    Returns:
        str: The capitalized full name string.
    """
    # Split the string into words based on spaces
    words = S.split()
    
    # Capitalize the first letter of each word and keep the rest as is
    capitalized_words = [word.capitalize() for word in words]
    
    # Join the capitalized words back into a single string with spaces
    return " ".join(capitalized_words)
```