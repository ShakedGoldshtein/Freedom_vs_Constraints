```python
def unique_date(a: int, b: int, c: int) -> str:
    def is_valid_date(yy: int, mm: int, dd: int) -> bool:
        if not (0 <= yy <= 99 and 1 <= mm <= 12):
            return False
        max_day = 31
        if mm in {4, 6, 9, 11}:
            max_day = 30
        elif mm == 2:
            max_day = 29 if (yy + 1900) % 4 == 0 and ((yy + 1900) % 100 != 0 or (yy + 1900) % 400 == 0) else 28
        return 1 <= dd <= max_day

    def generate_permutations(x: int, y: int, z: int) -> list[tuple[int, int, int]]:
        return [
            (x, y, z), (x, z, y),
            (y, x, z), (y, z, x),
            (z, x, y), (z, y, x)
        ]

    valid_dates = []
    for perm in generate_permutations(a, b, c):
        yy, mm, dd = perm
        if is_valid_date(yy, mm, dd):
            valid_dates.append(f"{yy:02d}/{mm:02d}/{dd:02d}")

    unique_dates = list(set(valid_dates))
    if not unique_dates:
        return "invalid"
    if len(unique_dates) > 1:
        return "ambiguous"
    return unique_dates[0]
```