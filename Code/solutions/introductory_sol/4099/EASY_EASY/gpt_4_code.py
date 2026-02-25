```python
def flip_bit(value, index):
    return value ^ (1 << (index - 1))
```