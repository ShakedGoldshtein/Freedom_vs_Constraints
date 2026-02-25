```python
def get_first_chars_of_words(text: str) -> str:
    """
    Extracts the first character of each word in a given string.

    Words are determined by splitting the string based on whitespace.
    Leading, trailing, and multiple internal spaces are handled automatically,
    ensuring that only actual words contribute a character.

    Args:
        text: The input string from which to extract the first characters.

    Returns:
        A new string composed of the first character of each word.
        Returns an empty string if the input string is empty or contains only whitespace.

    Raises:
        TypeError: If the input `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Split the string by whitespace. By default, str.split() handles multiple
    # spaces and leading/trailing spaces correctly, returning a list of non-empty words.
    words = text.split()

    # Create a list of the first character of each word.
    # The 'word' in 'words' will never be empty here due to how str.split() works.
    first_chars = [word[0] for word in words]

    # Join the collected first characters into a single string.
    return "".join(first_chars)
```