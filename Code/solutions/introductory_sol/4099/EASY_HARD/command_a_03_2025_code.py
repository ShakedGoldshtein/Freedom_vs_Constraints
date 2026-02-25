```python
def flip_bit(value: int, index: int) -> int:
    """
    Flips the bit at the given index in the binary representation of the value.

    Args:
        value (int): The integer value whose bit is to be flipped.
        index (int): The index of the bit to flip (1-based, starting from the least significant bit).

    Returns:
        int: The value with the specified bit flipped.
    """
    # Calculate the mask to flip the bit at the given index
    mask = 1 << (index - 1)
    
    # Use XOR to flip the bit
    return value ^ mask
```