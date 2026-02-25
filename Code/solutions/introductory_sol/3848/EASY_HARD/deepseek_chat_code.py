```python
from itertools import permutations

def unique_date(a, b, c):
    def is_valid_date(y, m, d):
        if not (0 <= y <= 99 and 1 <= m <= 12 and 1 <= d <= 31):
            return False
        
        if m in [4, 6, 9, 11] and d > 30:
            return False
        
        if m == 2:
            if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
                if d > 29:
                    return False
            else:
                if d > 28:
                    return False
        
        return True

    valid_dates = []
    for y, m, d in permutations([a, b, c]):
        if is_valid_date(y, m, d):
            valid_dates.append((y, m, d))
    
    if not valid_dates:
        return "invalid"
    
    unique_dates = set(valid_dates)
    if len(unique_dates) > 1:
        return "ambiguous"
    
    y, m, d = unique_dates.pop()
    return f"{y:02d}/{m:02d}/{d:02d}"
```