```python
def unique_date(a, b, c):
    from itertools import permutations
    numbers = sorted([a, b, c])
    dates = set()
    for perm in permutations(numbers):
        year, month, day = perm
        if month > 12 or day > 31 or year < 00 or year > 99:
            continue
        dates.add(f"{str(year).zfill(2)}/{str(month).zfill(2)}/{str(day).zfill(2)}")
    if len(dates) == 0:
        return 'invalid'
    elif len(dates) > 1:
        return 'ambiguous'
    else:
        return list(dates)[0]
```
