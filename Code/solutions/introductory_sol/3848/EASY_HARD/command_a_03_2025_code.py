```python
from itertools import permutations


def is_valid_date(year: int, month: int, day: int) -> bool:
    """Check if the given year, month, and day form a valid date in the 20th century.

    Args:
        year (int): The year to check (must be between 0 and 99).
        month (int): The month to check (must be between 1 and 12).
        day (int): The day to check (must be between 1 and the number of days in the month).

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    elif month == 2:
        return 1 <= day <= 28
    return False


def unique_date(a: int, b: int, c: int) -> str:
    """Determine if any ordering of the numbers forms a date from the 20th century.

    Args:
        a (int): The first integer in the range [0-99].
        b (int): The second integer in the range [0-99].
        c (int): The third integer in the range [0-99].

    Returns:
        str: The date in "YY/MM/DD" format if only one ordering forms a date,
             "ambiguous" if multiple orderings form dates, or "invalid" if no ordering forms a date.
    """
    dates: list[tuple[int, int, int]] = []
    for year, month, day in permutations([a, b, c]):
        if is_valid_date(year, month, day):
            dates.append((year, month, day))

    if len(dates) == 0:
        return "invalid"
    elif len(dates) > 1:
        return "ambiguous"
    else:
        year, month, day = dates[0]
        return f"{year:02}/{month:02}/{day:02}"
```