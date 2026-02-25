```python
def flip_bit(value, index):
    """
    Function to flip a bit of a given value at the specified index
    """
    # Using bitwise XOR to flip the bit at the specified index
    mask = 1 << (index - 1)
    result = value ^ mask
    return result
```