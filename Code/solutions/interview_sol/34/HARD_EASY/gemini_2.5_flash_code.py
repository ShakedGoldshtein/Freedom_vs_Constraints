```python
def _get_greatest_integer_for_n(n: int) -> str:
    """
    Calculates the greatest integer that can be displayed using exactly 'n' segments
    based on the problem's segment display rules.
    This function prioritizes maximizing the length of the integer, and then
    lexicographically maximizing its value.

    The segment counts for digits are:
    '0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6

    To maximize the integer:
    1. Maximize its length: Use digits requiring the fewest segments.
       The digit '1' uses 2 segments (minimum).
    2. Maximize lexicographical value for a given length: Place larger digits
       at more significant positions (leftmost).

    If n is even:
        All segments can be used by '1's, as '1' uses 2 segments.
        This maximizes length (n / 2 digits) and uses only '1's.
    If n is odd:
        We cannot form a number solely with '1's because 1s use an even number of segments.
        We must use at least one digit that uses an odd number of segments.
        To maintain maximal length and lexicographical value:
        - We choose '7' (3 segments) as the first digit. '7' uses the minimum
          odd number of segments, and it's a relatively large digit.
          Using '7' leaves `n - 3` segments, which is an even number.
        - The remaining `(n - 3) // 2` segments are then filled with '1's to
          maximize the length of the number.
    This strategy ensures the longest possible number, or the longest possible number
    with the largest leading digit if `n` is odd.

    Args:
        n: The maximum number of segments that can be turned on.
           Guaranteed: 2 <= n <= 10^5.

    Returns:
        A string representing the greatest integer that can be displayed.
    """
    if n % 2 == 0:
        # If n is even, the maximum number of digits is n // 2.
        # Using all '1's (each takes 2 segments) creates the longest number.
        # Example: n=4 -> "11"
        return '1' * (n // 2)
    else:
        # If n is odd, we need one digit that uses an odd number of segments.
        # The digit '7' uses 3 segments (the smallest odd segment count) and is relatively large.
        # Place '7' as the leading digit.
        # This leaves (n - 3) segments, which is now an even number.
        remaining_segments = n - 3
        # Fill the rest with '1's to maximize length.
        # Example: n=3 -> "7"
        # Example: n=5 -> "71" (7 uses 3, 1 uses 2. Total 5 segments)
        return '7' + '1' * (remaining_segments // 2)


def solve(n_values: list[int]) -> list[str]:
    """
    Processes multiple test cases, calculating the greatest integer for each
    given maximum segment limit.

    Args:
        n_values: A list of integers, where each integer `n` represents the
                  maximum number of segments for a specific test case.
                  Constraints: 1 <= len(n_values) <= 100,
                               2 <= n_values[i] <= 10^5 for each i,
                               sum(n_values) <= 10^5.

    Returns:
        A list of strings, where each string is the greatest integer
        corresponding to the respective `n` value in `n_values`.
        The results are in the same order as the input `n_values`.
    """
    results = []
    for n in n_values:
        results.append(_get_greatest_integer_for_n(n))
    return results
```