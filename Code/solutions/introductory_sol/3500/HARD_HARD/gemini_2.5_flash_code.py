```python
def remove_exclamation_marks(input_string: str) -> str:
    """
    Removes all exclamation marks from a given string.

    This function iterates through the input string and constructs a new string
    that excludes any exclamation mark characters ('!'). It is designed for
    optimal time and space complexity for this specific task.

    Args:
        input_string (str): The string from which exclamation marks should be removed.

    Returns:
        str: A new string with all exclamation marks removed.

    Raises:
        TypeError: If the input_string is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # The string.replace() method is highly optimized in Python's C implementation
    # for this type of operation, making it the most efficient solution
    # in terms of both time and constant-factor performance.
    # Time Complexity: O(N), where N is the length of the input_string,
    #                  as it needs to potentially scan the entire string.
    # Space Complexity: O(N) in the worst case (if no exclamation marks are removed),
    #                   as it creates a new string to store the result.
    #                   More precisely, O(K) where K is the length of the resulting string.
    return input_string.replace('!', '')
```