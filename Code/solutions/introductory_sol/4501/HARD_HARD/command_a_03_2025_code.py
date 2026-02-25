```python
def inside_out_word(word: str) -> str:
    """
    Turns a single word 'inside out' by swapping internal and external letters.
    If the word length is odd, the middle letter remains in place.

    Args:
        word (str): The input word to be transformed

    Returns:
        str: The transformed word with letters swapped
    """
    length = len(word)
    if length <= 1:
        return word

    # Calculate middle index for odd-length words
    mid = length // 2

    # Split word into left, middle (if odd), and right parts
    left = word[:mid]
    middle = word[mid] if length % 2 else ''
    right = word[mid + 1:] if length % 2 else word[mid:]

    # Reverse left and right parts and combine with middle
    return left[::-1] + middle + right[::-1]

def solve(x: str) -> str:
    """
    Processes a string of words, turning each word 'inside out'.

    Args:
        x (str): Input string containing words separated by spaces

    Returns:
        str: Transformed string with each word turned inside out
    """
    return ' '.join(inside_out_word(word) for word in x.split())
```