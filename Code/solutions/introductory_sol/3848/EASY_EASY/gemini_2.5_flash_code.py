```python
import itertools

def unique_date(a, b, c):
    """
    Determines if any ordering of three given integers forms a unique 20th-century date.

    Args:
        a, b, c (int): Three integers in the range [0-99].

    Returns:
        str: "invalid" if no ordering forms a date.
             "ambiguous" if multiple distinct orderings form dates.
             "YY/MM/DD" if only one ordering forms a date.
    """

    def is_valid_date_components(yy, mm, dd):
        """
        Checks if the given year (YY), month (MM), and day (DD) form a valid 20th-century date.
        YY is the two-digit year (0-99), implicitly 19YY.
        """
        if not (1 <= mm <= 12):
            return False
        if not (1 <= dd <= 31): # Initial check for day within general range
            return False

        # Max days for each month (0-indexed dummy, then Jan-Dec)
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        max_day = days_in_month[mm]

        if mm == 2:  # February
            # Leap year rule for 20th century (1900-1999)
            # A year YYYY is a leap year if:
            # - divisible by 4, UNLESS
            # - divisible by 100 but NOT by 400.
            #
            # For 19YY (where YY is 0-99):
            # - 1900 (yy=0) is divisible by 100 but not 400, so it's NOT a leap year.
            # - Other years (1901-1999) are leap if YY is divisible by 4.
            is_leap = (yy != 0 and yy % 4 == 0)
            if is_leap:
                max_day = 29
            else:
                max_day = 28

        return 1 <= dd <= max_day

    nums = [a, b, c]
    found_dates = set()

    # Iterate through all 3! = 6 permutations of the three numbers.
    # Each permutation (p1, p2, p3) is tried as (YY, MM, DD).
    for p in itertools.permutations(nums):
        yy, mm, dd = p
        if is_valid_date_components(yy, mm, dd):
            # Format the date as "YY/MM/DD" with leading zeros
            found_dates.add(f"{yy:02d}/{mm:02d}/{dd:02d}")

    num_found_dates = len(found_dates)

    if num_found_dates == 0:
        return "invalid"
    elif num_found_dates == 1:
        # Since there's only one, we can safely pop it from the set
        return found_dates.pop()
    else:
        return "ambiguous"
```