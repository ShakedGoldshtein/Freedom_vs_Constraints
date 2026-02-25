```python
def flip_bit(value, index):
    mask = 1 << (index - 1)
    return value ^ mask
```