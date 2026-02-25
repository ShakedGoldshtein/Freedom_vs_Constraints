```python
def encode(s):
    return ''.join(str(ord(c) - 96) if c.isalpha() else c for c in s.lower())
```