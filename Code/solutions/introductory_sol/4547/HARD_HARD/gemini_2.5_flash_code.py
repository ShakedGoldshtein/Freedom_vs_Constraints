```python
def _count_zeros_vs_ones(char_code: int) -> bool:
    """
    Checks if the binary representation of an integer has strictly more zeros than ones.
    Leading zeros are naturally excluded by Python's `bin()` function output
    (e.g., `bin(65)` is '0b1000001', not '0b01000001').

    This function is an internal helper and assumes `char_code` is a valid integer.

    Args:
        char_code: The integer (typically a character's ASCII or Unicode code point)
                   whose binary representation will be analyzed.

    Returns:
        True if the count of '0's in the binary representation is strictly
        greater than the count of '1's; False otherwise.
    """
    # Convert the integer to its binary representation string.
    # `bin()` returns a string prefixed with '0b', which we slice off.
    # Example: bin(65) -> '0b1000001', so binary_repr becomes '1000001'.
    binary_repr = bin(char_code)[2:]

    # Count occurrences of '0' and '1' in the binary string.
    zeros_count = binary_repr.count('0')
    ones_count = binary_repr.count('1')

    return zeros_count > ones_count


def moreZeros(input_string: str) -> list[str]:
    """
    Filters characters from an input string based on the binary representation
    of their ASCII (or Unicode) values.

    A character is included in the output list if its binary representation
    contains strictly more zeros than ones. Duplicate characters are removed,
    keeping only their first occurrence, and the order of appearance
    from the input string is preserved.

    Args:
        input_string: The string to process. Must be a string.
                      Per problem statement, this string will have length > 0.

    Returns:
        A list of unique characters (each as a string of length 1) that satisfy
        the 'more zeros than ones' condition. The characters in the list are
        ordered by their first appearance in the input string.

    Raises:
        TypeError: If `input_string` is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    # `result_chars` will store the qualifying characters in order.
    # `seen_chars` is a set used for efficient O(1) average time complexity
    # lookup to track and prevent duplicate characters from being added.
    result_chars: list[str] = []
    seen_chars: set[str] = set()

    for char in input_string:
        # Optimize by checking if the character has already been added
        # before performing the potentially more expensive binary conversion.
        if char in seen_chars:
            continue

        # Get the integer (ASCII/Unicode) value of the character.
        char_code = ord(char)

        # Check the condition: more zeros than ones in binary representation.
        if _count_zeros_vs_ones(char_code):
            result_chars.append(char)
            seen_chars.add(char)
            
    return result_chars
```