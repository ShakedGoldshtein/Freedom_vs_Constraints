```python
def solve(x: str) -> str:
    """
    Turns each word in the input string 'inside out'.

    For each word, the internal letters move out, and the external letters move toward the centre.
    If the word length is even, all letters move. If the length is odd, the middle letter remains in place.

    Args:
        x (str): The input string containing words to be turned 'inside out'.

    Returns:
        str: The modified string with each word turned 'inside out'.
    """
    words = x.split()
    result = []

    for word in words:
        n = len(word)
        if n <= 1:
            result.append(word)
            continue

        # Calculate the middle index for odd-length words
        mid = n // 2

        # Split the word into left and right halves
        left = word[:mid]
        right = word[mid + (n % 2):]  # Exclude the middle character if word length is odd

        # Reverse the left and right halves and combine them
        if n % 2 == 0:
            # For even-length words, combine the reversed halves
            new_word = left[::-1] + right[::-1]
        else:
            # For odd-length words, combine the reversed halves with the middle character
            new_word = left[::-1] + word[mid] + right[::-1]

        result.append(new_word)

    return ' '.join(result)
```