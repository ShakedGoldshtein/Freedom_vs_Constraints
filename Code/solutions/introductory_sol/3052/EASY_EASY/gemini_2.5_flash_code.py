```python
def remove(s: str) -> str:
    """
    Removes all exclamation marks from a sentence except at the end.

    Args:
        s: The input string.

    Returns:
        The string with internal exclamation marks removed, but trailing ones preserved.
    """
    if not s:
        return ""

    # Count trailing exclamation marks
    trailing_exclamations_count = 0
    for char in reversed(s):
        if char == '!':
            trailing_exclamations_count += 1
        else:
            break

    # Separate the string into the part before trailing '!'s and the trailing '!'s themselves
    # Python's slicing handles trailing_exclamations_count=0 gracefully:
    # s[:-0] becomes s[:len(s)], which is the entire string.
    # s[-0:] becomes s[len(s):], which is an empty string.
    prefix_part = s[:-trailing_exclamations_count]
    suffix_part = s[-trailing_exclamations_count:]

    # Remove all '!' from the prefix part
    cleaned_prefix_part = prefix_part.replace('!', '')

    # Combine the cleaned prefix with the original trailing '!'s
    return cleaned_prefix_part + suffix_part
```