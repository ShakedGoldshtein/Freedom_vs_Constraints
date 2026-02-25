```python
import itertools

def _is_leap_year(year_yy: int) -> bool:
    """
    Checks if a year in the 20th century (1900 + year_yy) is a leap year.

    Args:
        year_yy: The two-digit year (0-99) representing 1900-1999.

    Returns:
        True if the year is a leap year, False otherwise.
    """
    full_year = 1900 + year_yy
    # A year is a leap year if it is divisible by 4,
    # unless it is divisible by 100 but not by 400.
    # For the 20th century (1900-1999):
    # - 1900 is divisible by 100 but not 400, so NOT a leap year.
    # - Other years like 1904, 1996 are divisible by 4 and not 100, so ARE leap years.
    return (full_year % 4 == 0 and full_year % 100 != 0) or (full_year % 400 == 0)

def _get_days_in_month(month: int, year_yy: int) -> int:
    """
    Returns the number of days in a given month for a specific 20th-century year.

    Args:
        month: The month (1-12).
        year_yy: The two-digit year (0-99) representing 1900-1999.

    Returns:
        The number of days in the month, or 0 if the month is invalid.
    """
    if not (1 <= month <= 12):
        return 0  # Invalid month

    days_in_months = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if month == 2 and _is_leap_year(year_yy):
        return 29
    return days_in_months[month]

def _is_valid_date_components(year_yy: int, month_mm: int, day_dd: int) -> bool:
    """
    Checks if a combination of year, month, and day components forms a valid 20th-century date.

    Args:
        year_yy: Two-digit year (0-99).
        month_mm: Month (1-12).
        day_dd: Day (1-31).

    Returns:
        True if the date is valid, False otherwise.
    """
    # Year component (0-99) is considered valid for the YY part of a 20th-century date
    # as per problem definition for the input range.
    # We only need to validate month and day.

    if not (1 <= month_mm <= 12):
        return False

    max_days = _get_days_in_month(month_mm, year_yy)
    if not (1 <= day_dd <= max_days):
        return False

    return True

def unique_date(val1: int, val2: int, val3: int) -> str:
    """
    Determines if any ordering of three given numbers forms a unique 20th-century date.

    The input numbers are expected to be integers in the range [0-99].
    A 20th-century date is represented as "YY/MM/DD", where YY is 00-99 (meaning 1900-1999).

    Args:
        val1: The first integer (0-99).
        val2: The second integer (0-99).
        val3: The third integer (0-99).

    Returns:
        - "invalid" if no ordering forms a valid date.
        - "ambiguous" if multiple distinct orderings form valid dates.
        - The date string "YY/MM/DD" if only one ordering forms a valid date.
    """
    numbers = [val1, val2, val3]
    found_dates = set()

    # Iterate through all permutations of the three numbers.
    # Each permutation (p_yy, p_mm, p_dd) is a candidate for (YY, MM, DD).
    # Since there are only 3 numbers, there are 3! = 6 permutations.
    # This results in O(1) time complexity.
    for p_yy, p_mm, p_dd in itertools.permutations(numbers):
        if _is_valid_date_components(p_yy, p_mm, p_dd):
            # Format the date string with zero-padding for single-digit numbers.
            found_dates.add(f"{p_yy:02d}/{p_mm:02d}/{p_dd:02d}")

    num_found_dates = len(found_dates)

    if num_found_dates == 0:
        return "invalid"
    elif num_found_dates > 1:
        return "ambiguous"
    else:  # num_found_dates == 1
        return found_dates.pop()

```