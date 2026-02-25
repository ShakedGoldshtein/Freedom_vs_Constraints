```python
def remove_exclamation_marks(sentence: str) -> str:
    """
    Removes all exclamation marks from a sentence except those at the very end.

    This function iterates from the end of the sentence to identify the block of
    trailing exclamation marks. It then processes the remaining part of the
    sentence to remove any other exclamation marks and finally combines the
    cleaned prefix with the preserved trailing marks.

    Args:
        sentence: The input string from which to remove exclamation marks.

    Returns:
        The modified string with only trailing exclamation marks preserved.

    Raises:
        TypeError: If the input 'sentence' is not a string.
    """
    if not isinstance(sentence, str):
        raise TypeError("Input 'sentence' must be a string.")

    # Handle empty string or string with no exclamation marks directly for efficiency,
    # though the main logic handles these correctly as well.
    if not sentence:
        return ""
    
    # Step 1: Find the boundary between the main part of the sentence
    # and any trailing exclamation marks.
    # We iterate backwards to find the first character that is not an exclamation mark.
    idx = len(sentence) - 1
    while idx >= 0 and sentence[idx] == '!':
        idx -= 1

    # Step 2: Separate the sentence into two parts:
    # the part before any trailing exclamation marks (prefix)
    # and the block of trailing exclamation marks (trailing_exclamations).
    # 'idx + 1' points to the first trailing exclamation mark, or `len(sentence)`
    # if there are no trailing exclamation marks.
    trailing_exclamations = sentence[idx + 1:]
    
    # The 'prefix' is the segment of the sentence up to, and including,
    # the last non-exclamation mark found from the right.
    prefix = sentence[:idx + 1]

    # Step 3: Remove all exclamation marks from the 'prefix'.
    # The `str.replace()` method is efficient for this operation and
    # creates a new string without modifying the original.
    cleaned_prefix = prefix.replace('!', '')

    # Step 4: Combine the cleaned prefix with the preserved trailing exclamation marks.
    return cleaned_prefix + trailing_exclamations
```