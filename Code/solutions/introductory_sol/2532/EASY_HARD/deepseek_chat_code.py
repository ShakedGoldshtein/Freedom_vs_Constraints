```python
def thousandSeparator(n):
    s = str(n)
    result = []
    for i, ch in enumerate(reversed(s)):
        if i > 0 and i % 3 == 0:
            result.append('.')
        result.append(ch)
    return ''.join(reversed(result))
```