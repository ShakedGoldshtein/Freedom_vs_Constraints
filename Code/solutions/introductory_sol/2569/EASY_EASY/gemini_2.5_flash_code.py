```python
def solve(s):
    result_chars = []
    capitalize_next = True  # Flag to determine if the next alphabetic character should be capitalized

    for char in s:
        if char == ' ':
            result_chars.append(char)
            capitalize_next = True  # A space means the next non-space character is potentially the start of a new word
        else:
            if capitalize_next:
                # This character is at the start of a potential word
                if char.isalpha():
                    result_chars.append(char.upper())
                else:
                    # If it's not alphabetic (e.g., '1', '#'), it remains unchanged
                    # but we are now "inside" a word, so don't capitalize the next char
                    result_chars.append(char)
                capitalize_next = False  # Turn off the flag as we've processed the first character of this segment
            else:
                # This character is not the first in its segment
                if char.isalpha():
                    result_chars.append(char.lower())  # Lowercase subsequent alphabetic characters
                else:
                    result_chars.append(char)  # Non-alphabetic characters remain unchanged

    return "".join(result_chars)
```