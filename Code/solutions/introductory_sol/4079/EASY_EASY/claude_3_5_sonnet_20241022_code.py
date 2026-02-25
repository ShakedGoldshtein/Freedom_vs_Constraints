```python
def encode(str):
    return ''.join(str(ord(c) - 96) if c.islower() else str(ord(c) - 64) if c.isupper() else c for c in str)
```