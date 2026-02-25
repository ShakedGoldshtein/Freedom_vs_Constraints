```python
def triple_trouble(a, b, c):
    return ''.join([x + y + z for x, y, z in zip(a, b, c)])
```