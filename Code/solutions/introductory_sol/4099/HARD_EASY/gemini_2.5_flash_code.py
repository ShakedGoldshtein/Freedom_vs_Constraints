```python
def flip_bit(value: int, index: int) -> int:
    """
    Flips the bit at a specified 1-based index in an integer value.

    The bits are numbered from the least significant bit (index 1).
    If the bit at the given index in the `value` is 0, it becomes 1.
    If it's 1, it becomes 0. This operation effectively toggles the bit.

    The `index` can be greater than the number of bits currently represented
    by `value`. In such cases, the number's effective length is extended,
    and a 0-bit at that higher index is flipped to a 1.

    Args:
        value: The integer value whose bit is to be flipped.
               Can be positive, zero, or negative (bit-flipping on negative
               numbers follows standard two's complement behavior for Python integers).
        index: The 1-based index of the bit to flip.
               Must be a positive integer (index >= 1).

    Returns:
        The integer value with the bit at the specified index flipped.

    Raises:
        ValueError: If `index` is less than 1.

    Examples:
        >>> flip_bit(15, 4)
        7  # 15 (binary 1111) becomes 7 (binary 0111) after flipping 4th bit.
        >>> flip_bit(15, 5)
        31 # 15 (binary 01111) becomes 31 (binary 11111) after flipping 5th bit (which was 0).
        >>> flip_bit(3, 8)
        131 # 3 (binary 00000011) becomes 131 (binary 10000011) after flipping 8th bit (which was 0).
        >>> flip_bit(0, 1)
        1  # 0 (binary 0) becomes 1 (binary 1).
        >>> flip_bit(1, 1)
        0  # 1 (binary 1) becomes 0 (binary 0).
        >>> flip_bit(1, 2)
        3  # 1 (binary 01) becomes 3 (binary 11).
    """
    if not isinstance(index, int) or index < 1:
        raise ValueError("Bit index must be a positive integer (1 or greater).")

    # Convert the 1-based index to a 0-based bit position for bitwise operations.
    bit_position_0based = index - 1

    # Create a mask with only the bit at the desired position set.
    # For example, if bit_position_0based is 3, mask will be 0b1000 (decimal 8).
    mask = 1 << bit_position_0based

    # Use the XOR operator (^) to flip the bit.
    # XORing with a mask that has only one bit set will flip that specific bit:
    # 0 ^ 1 = 1 (flips 0 to 1)
    # 1 ^ 1 = 0 (flips 1 to 0)
    return value ^ mask
```