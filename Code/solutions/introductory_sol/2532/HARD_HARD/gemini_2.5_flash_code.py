```python
def format_thousands_separator(n: int) -> str:
    """
    Formats an integer n by adding a dot (".") as the thousands separator.

    The function processes non-negative integers as specified by the constraints.
    It constructs the formatted string by identifying the initial segment
    and then grouping subsequent digits into sets of three, separated by dots.

    Args:
        n: The integer to format. Constraints: 0 <= n < 2^31.

    Returns:
        A string representation of the integer with thousands separators.

    Time Complexity: O(log10(n)) - proportional to the number of digits in n,
                     as string conversion and concatenation operations depend on the digit count.
    Space Complexity: O(log10(n)) - proportional to the number of digits in n,
                      for storing the string representation and the list of parts.
    """
    s_n = str(n)
    length = len(s_n)

    # If the number has 3 or fewer digits, no separator is needed.
    if length <= 3:
        return s_n

    parts = []

    # Calculate the length of the first segment.
    # For example:
    # "1234" (length 4) -> (4-1)%3+1 = 1. First segment is "1".
    # "12345" (length 5) -> (5-1)%3+1 = 2. First segment is "12".
    # "123456" (length 6) -> (6-1)%3+1 = 3. First segment is "123".
    first_segment_len = (length - 1) % 3 + 1
    
    # Add the first segment to the list of parts.
    parts.append(s_n[0:first_segment_len])

    # Add subsequent segments, each of 3 digits, separated by dots.
    # The loop starts from the end of the first segment.
    for i in range(first_segment_len, length, 3):
        parts.append(".")
        parts.append(s_n[i:i+3])

    # Join all parts to form the final formatted string.
    return "".join(parts)
```