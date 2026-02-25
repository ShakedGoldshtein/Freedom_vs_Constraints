```python
def solve(n: int) -> str:
    """
    Calculates the greatest integer that can be displayed using no more than n segments.

    The segment counts for digits are:
    0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6.

    To maximize the integer:
    1. Maximize the number of digits. This is achieved by using digits that require
       the fewest segments. The digit '1' uses 2 segments, which is the minimum.
    2. If multiple numbers have the maximum number of digits, choose the lexicographically
       largest one (i.e., put larger digits at the beginning).

    If n is even:
        We can use n // 2 '1's. Each '1' uses 2 segments. This forms the maximum
        possible number of digits (n // 2) and uses exactly n segments.
        Example: n=4 -> "11" (2 '1's)
        Example: n=6 -> "111" (3 '1's)

    If n is odd:
        We cannot form all '1's and use all segments, as '1's use an even number
        of segments. To use all segments, we must include at least one digit
        that uses an odd number of segments. The digit '7' uses 3 segments,
        which is the smallest odd segment count.
        By starting with one '7' (3 segments), we are left with (n - 3) segments.
        Since n is odd, (n - 3) is even. We can then use (n - 3) // 2 '1's
        to consume the remaining even segments.
        This forms 1 + (n - 3) // 2 digits, which is the maximum possible.
        Placing the '7' at the beginning results in the lexicographically largest
        number among those with the maximum number of digits.
        Example: n=3 -> "7" (one '7')
        Example: n=5 -> "71" (one '7', one '1')

    Args:
        n: The maximum number of segments allowed (2 <= n <= 10^5).

    Returns:
        A string representing the greatest integer that can be displayed.
        The result can be very large and may not fit in standard integer types,
        so a string is used for its representation.
    """
    if n % 2 == 0:
        # If n is even, we can form n // 2 '1's
        return "1" * (n // 2)
    else:
        # If n is odd, start with '7' and then add '1's for remaining segments
        return "7" + "1" * ((n - 3) // 2)

```