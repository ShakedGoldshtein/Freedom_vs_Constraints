```python
from itertools import permutations
from datetime import datetime

def is_valid_date(year: int, month: int, day: int) -> bool:
    """Check if the given year, month, and day form a valid date in the 20th century."""
    try:
        datetime(year + 1900, month, day)
        return True
    except ValueError:
        return False

def unique_date(a: int, b: int, c: int) -> str:
    """
    Determine if any ordering of the numbers forms a date from the 20th century.

    Args:
        a (int): First integer in the range [0-99].
        b (int): Second integer in the range [0-99].
        c (int): Third integer in the range [0-99].

    Returns:
        str: The date in "YY/MM/DD" format if unique, "ambiguous" if multiple dates are valid, or "invalid" if no valid date exists.
    """
    numbers = [a, b, c]
    valid_dates = []

    # Generate all permutations of the numbers
    for perm in permutations(numbers):
        year, month, day = perm
        if 1 <= month <= 12 and 1 <= day <= 31 and is_valid_date(year, month, day):
            valid_dates.append(f"{year:02}/{month:02}/{day:02}")

    # Determine the result based on the number of valid dates
    if len(valid_dates) == 0:
        return "invalid"
    elif len(valid_dates) > 1:
        return "ambiguous"
    else:
        return valid_dates[0]
```