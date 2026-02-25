```python
def cal_n_bug(total_heads: int, total_legs: int, total_wing_pairs: int) -> list[int]:
    """
    Calculates the number of spiders, butterflies, and dragonflies given
    the total number of heads, legs, and wing pairs.

    A spider has 1 head, 8 legs, 0 wing pairs.
    A butterfly has 1 head, 6 legs, 1 wing pair.
    A dragonfly has 1 head, 6 legs, 2 wing pairs.

    Args:
        total_heads (int): The total number of heads.
        total_legs (int): The total number of legs.
        total_wing_pairs (int): The total number of wing pairs.

    Returns:
        list[int]: A list [n_spider, n_butterfly, n_dragonfly] if a valid
                   non-negative integer solution exists.
                   Returns [-1, -1, -1] otherwise (e.g., negative counts,
                   non-integer counts, or biologically impossible scenarios).
    """
    # Let n_spider = number of spiders (s)
    # Let n_butterfly = number of butterflies (b)
    # Let n_dragonfly = number of dragonflies (d)

    # We have a system of three linear equations:
    # 1. Heads: s + b + d = total_heads
    # 2. Legs:  8s + 6b + 6d = total_legs
    # 3. Wings: 0s + 1b + 2d = total_wing_pairs

    # From equation (1), we can express s:
    # s = total_heads - b - d

    # Substitute 's' into equation (2):
    # 8 * (total_heads - b - d) + 6b + 6d = total_legs
    # 8 * total_heads - 8b - 8d + 6b + 6d = total_legs
    # 8 * total_heads - 2b - 2d = total_legs
    # Rearranging for (2b + 2d):
    # 2b + 2d = 8 * total_heads - total_legs

    # Let's call the right side 'intermediate_leg_expression'.
    # This value must be non-negative and even for 'b + d' to be a non-negative integer.
    intermediate_leg_expression = 8 * total_heads - total_legs
    if intermediate_leg_expression < 0 or intermediate_leg_expression % 2 != 0:
        return [-1, -1, -1]

    # Now we have:
    # 4. b + d = intermediate_leg_expression / 2
    sum_b_d = intermediate_leg_expression // 2  # Use integer division

    # We now have a simplified system of two equations for 'b' and 'd':
    # A. b + d = sum_b_d         (from equation 4)
    # B. b + 2d = total_wing_pairs (from equation 3)

    # Subtract equation A from equation B:
    # (b + 2d) - (b + d) = total_wing_pairs - sum_b_d
    # d = total_wing_pairs - sum_b_d
    n_dragonfly = total_wing_pairs - sum_b_d

    # Check if the number of dragonflies is valid (non-negative).
    if n_dragonfly < 0:
        return [-1, -1, -1]

    # Substitute 'd' back into equation A to find 'b':
    # b = sum_b_d - d
    n_butterfly = sum_b_d - n_dragonfly

    # Check if the number of butterflies is valid (non-negative).
    if n_butterfly < 0:
        return [-1, -1, -1]

    # Substitute 'b' and 'd' back into the expression for 's' (from equation 1):
    # s = total_heads - b - d
    n_spider = total_heads - n_butterfly - n_dragonfly

    # Check if the number of spiders is valid (non-negative).
    if n_spider < 0:
        return [-1, -1, -1]

    # All counts must be non-negative integers. Our step-by-step calculations
    # ensure integer results if the initial parity check holds for 'intermediate_leg_expression'.

    return [n_spider, n_butterfly, n_dragonfly]
```