```python
def unique_date(a, b, c):
    def is_valid_date(y, m, d):
        if not (0 <= y <= 99 and 1 <= m <= 12 and 1 <= d <= 31):
            return False
        
        if m in {4, 6, 9, 11} and d > 30:
            return False
        
        if m == 2:
            if (y % 4 == 0 and y != 0) or (y == 0 and d == 29):
                return d <= 29
            return d <= 28
        
        return True

    def format_date(y, m, d):
        return f"{y:02d}/{m:02d}/{d:02d}"

    numbers = [a, b, c]
    valid_dates = []
    
    for y, m, d in [
        (numbers[0], numbers[1], numbers[2]),
        (numbers[0], numbers[2], numbers[1]),
        (numbers[1], numbers[0], numbers[2]),
        (numbers[1], numbers[2], numbers[0]),
        (numbers[2], numbers[0], numbers[1]),
        (numbers[2], numbers[1], numbers[0])
    ]:
        if is_valid_date(y, m, d):
            date_str = format_date(y, m, d)
            if date_str not in valid_dates:
                valid_dates.append(date_str)
    
    if not valid_dates:
        return "invalid"
    elif len(valid_dates) > 1:
        return "ambiguous"
    else:
        return valid_dates[0]
```