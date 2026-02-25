```python
def format_with_thousands_separator(n):
    if n == 0:
        return "0"
    s = []
    count = 0
    while n > 0:
        digit = n % 10
        s.append(str(digit))
        count += 1
        if count % 3 == 0 and n // 10 != 0:
            s.append('.')
        n = n // 10
    return ''.join(reversed(s))
```