```python
import collections

def _transform_word(word: str) -> str:
    """
    Transforms a single word by turning its internal letters out and external letters in.

    For even-length words, the first half of the word is reversed, and the second half
    is reversed. These two reversed halves are then concatenated.
    Example: 'taxi' (first half 'ta', second half 'xi') becomes 'at' + 'ix' = 'atix'.

    For odd-length words, the middle character remains in its position. The prefix
    (letters before the middle) is reversed, and the suffix (letters after the middle)
    is reversed. These are then concatenated around the middle character.
    Example: 'taxis' (prefix 'ta', middle 'x', suffix 'is') becomes 'at' + 'x' + 'si' = 'atxsi'.

    Args:
        word: The word string to transform.

    Returns:
        The transformed word string.
    """
    n = len(word)

    if n == 0:
        return ""

    if n % 2 == 0:  # Even length word
        # Split into two equal halves
        midpoint = n // 2
        first_half = word[0:midpoint]
        second_half = word[midpoint:n]
        
        # Reverse each half and concatenate
        return first_half[::-1] + second_half[::-1]
    else:  # Odd length word
        # Find the middle character's index
        mid_idx = n // 2
        
        # Extract prefix, middle character, and suffix
        prefix = word[0:mid_idx]
        middle_char = word[mid_idx]
        suffix = word[mid_idx + 1:n]
        
        # Reverse prefix and suffix, then concatenate with the middle character
        return prefix[::-1] + middle_char + suffix[::-1]

def inside_out_words(text_string: str) -> str:
    """
    Transforms each word in the input string by turning it 'inside out'.

    Words are separated by whitespace. Multiple spaces are treated as a single separator,
    and leading/trailing spaces are handled by the splitting mechanism.

    Args:
        text_string: The input string containing words to be transformed.

    Returns:
        A new string where each word has been turned 'inside out',
        separated by single spaces. Returns an empty string if the input
        is empty or consists only of whitespace.
    """
    # Handle empty string or string with only whitespace gracefully.
    # str.split() without arguments handles multiple spaces and leading/trailing
    # spaces, returning an empty list if the string is empty or just spaces.
    words = text_string.split()
    
    # Process each word using the helper function
    transformed_words = []
    for word in words:
        transformed_words.append(_transform_word(word))
    
    # Join the transformed words back into a single string with spaces
    return " ".join(transformed_words)
```