```python
def capitalize_name(full_name: str) -> str:
    """
    Capitalizes the first and last names in a full name string appropriately.

    Args:
        full_name: A string containing the full name with words separated by spaces.
                  Words may contain alphanumeric characters.

    Returns:
        A new string where the first letter of each word is capitalized (if it's a letter),
        and the rest are lowercase. Non-letter starting words remain unchanged.
    """
    def capitalize_word(word: str) -> str:
        if not word:
            return word
        first_char = word[0]
        if first_char.isalpha():
            return first_char.upper() + word[1:].lower()
        return word

    words = full_name.split(' ')
    capitalized_words = [capitalize_word(word) for word in words]
    return ' '.join(capitalized_words)
```