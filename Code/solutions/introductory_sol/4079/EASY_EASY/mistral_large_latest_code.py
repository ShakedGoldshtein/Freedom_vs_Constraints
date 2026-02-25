```python
def encode(s):
    return ''.join(str(ord(c) - ord('a') + 1) if 'a' <= c <= 'z' else
                   str(ord(c) - ord('A') + 1) if 'A' <= c <= 'Z' else c
                   for c in s)
```