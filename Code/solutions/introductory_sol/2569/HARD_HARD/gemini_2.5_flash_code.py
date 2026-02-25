```python
def capitalize_full_name(s: str) -> str:
    """
    Capitalizes a full name according to passport requirements.

    Ensures that the first character of each word that starts with an alphabetic character
    is capitalized, while preserving original spacing and handling words starting
    with non-alphabetic characters (e.g., digits) by leaving them unchanged.

    Args:
        s: The full name string to capitalize. Consists of alphanumeric characters and spaces.
           Constraints: 0 < len(s) < 1000.

    Returns:
        The capitalized string.
    """
    # The problem statement constraints specify 0 < len(S),
    # so an empty string input is not expected.
    # However, for production-grade robustness, handling it gracefully is good practice.
    if not s:
        return ""

    result_chars = []
    # This flag tracks whether the next character encountered should be considered
    # as the potential start of a new word that could be capitalized.
    # It starts as True because the very first character of the string
    # is always considered the start of the first word.
    capitalize_next = True

    for char in s:
        if capitalize_next and char.isalpha():
            # If it's the start of a word and an alphabetic character, capitalize it.
            result_chars.append(char.upper())
            capitalize_next = False  # The first letter of this word has been handled.
        else:
            # If not the start of a word, or not an alphabetic character, keep it as is.
            result_chars.append(char)
            # Update capitalize_next: if the current character is a space,
            # the next character could be the start of a new word.
            # Otherwise (it's part of the current word or a non-alpha character),
            # capitalize_next remains False.
            capitalize_next = char.isspace()

    return "".join(result_chars)
```