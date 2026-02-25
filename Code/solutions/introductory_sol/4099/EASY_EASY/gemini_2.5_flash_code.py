```python
def flip_bit(value, index):
    """
    Flips the bit at the given 1-based index in the value.

    Args:
        value (int): The integer value.
        index (int): The 1-based index of the bit to flip.
                     (e.g., index 1 is the least significant bit).

    Returns:
        int: The value with the specified bit flipped.
    """
    # Create a mask with a 1 at the position corresponding to the (index-1)-th bit (0-indexed).
    # Since index is 1-based, we subtract 1 to get the 0-based shift amount.
    mask = 1 << (index - 1)
    
    # Use XOR to flip the bit at the mask's position.
    # If the bit is 0, XOR with 1 makes it 1.
    # If the bit is 1, XOR with 1 makes it 0.
    return value ^ mask
```