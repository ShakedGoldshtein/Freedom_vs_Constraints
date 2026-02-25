```python
def flip_bit(value, index):
    """
    Flips the bit at the given index (1-based from LSB) in the value.
    
    Args:
        value: Integer value whose bit needs to be flipped
        index: 1-based index from least significant bit (LSB)
    
    Returns:
        Integer with the bit at given index flipped
    """
    if not isinstance(value, int) or not isinstance(index, int):
        raise TypeError("Both value and index must be integers")
    
    if index < 1:
        raise ValueError("Index must be at least 1")
    
    # Convert to 0-based index from LSB
    bit_position = index - 1
    
    # Use XOR with a mask that has only the target bit set
    mask = 1 << bit_position
    return value ^ mask
```