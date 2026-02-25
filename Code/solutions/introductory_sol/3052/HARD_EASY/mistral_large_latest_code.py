```python
def remove(sentence: str) -> str:
    """
    Removes all exclamation marks from the sentence except those at the end.

    Args:
        sentence: Input string potentially containing exclamation marks.

    Returns:
        String with exclamation marks removed except those at the end.
    """
    if not sentence:
        return sentence

    # Split into non-exclamation and trailing exclamation parts
    end = len(sentence)
    while end > 0 and sentence[end - 1] == '!':
        end -= 1

    # Process the non-trailing part
    non_trailing = sentence[:end].replace('!', '')
    trailing = sentence[end:]

    return non_trailing + trailing
```