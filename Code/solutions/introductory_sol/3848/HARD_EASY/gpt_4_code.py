```python
from itertools import permutations

def unique_date(a, b, c):
    def is_date(year, month, day):
        return 0 < month < 13 and 0 < day < 32

    dates = list(filter(lambda x: is_date(*x), permutations((a, b, c), 3)))
    if not dates:
        return 'invalid'
    elif len(set(dates)) > 1:
        return 'ambiguous'
    else:
        return '{:02d}/{:02d}/{:02d}'.format(*dates[0])
```
