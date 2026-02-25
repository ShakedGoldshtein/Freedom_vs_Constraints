```python
def flip_bit(value: int, index: int) -> int:
    """
    Flips the bit at the given index (1-based) in the provided value
    
    Args:
        value: The integer value to modify
        index: The 1-based position of bit to flip (from LSB)
        
    Returns:
        The value with the bit at index flipped
    """
    # Create mask with 1 at the target position
    mask = 1 << (index - 1)
    
    # XOR with mask to flip the bit
    return value ^ mask
```