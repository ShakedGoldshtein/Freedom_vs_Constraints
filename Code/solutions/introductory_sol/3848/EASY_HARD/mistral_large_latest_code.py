```python
def unique_date(a, b, c):
    def is_valid_date(yy, mm, dd):
        if not (1 <= mm <= 12):
            return False
        if mm in {4, 6, 9, 11}:
            return 1 <= dd <= 30
        elif mm == 2:
            if (yy % 4 == 0 and yy % 100 != 0) or (yy % 400 == 0):
                return 1 <= dd <= 29
            else:
                return 1 <= dd <= 28
        else:
            return 1 <= dd <= 31

    permutations = [
        (a, b, c),
        (a, c, b),
        (b, a, c),
        (b, c, a),
        (c, a, b),
        (c, b, a)
    ]

    valid_dates = []
    for yy, mm, dd in permutations:
        if 0 <= yy <= 99 and 1 <= mm <= 12 and 1 <= dd <= 31:
            if is_valid_date(yy, mm, dd):
                date_str = f"{yy:02d}/{mm:02d}/{dd:02d}"
                if date_str not in valid_dates:
                    valid_dates.append(date_str)

    if not valid_dates:
        return "invalid"
    elif len(valid_dates) > 1:
        return "ambiguous"
    else:
        return valid_dates[0]
```