```python
def cal_n_bug(total_heads, total_legs, total_wing_pairs):
    """
    Calculates the number of spiders, butterflies, and dragonflies given total heads, legs, and wing pairs.

    A spider has 8 legs and 0 pairs of wings.
    A butterfly has 6 legs and 1 pair of wings.
    A dragonfly has 6 legs and 2 pairs of wings.
    All bugs have 1 head.

    Args:
        total_heads (int): The total number of heads.
        total_legs (int): The total number of legs.
        total_wing_pairs (int): The total number of pairs of wings.

    Returns:
        list: A list [n_spider, n_butterfly, n_dragonfly] if a valid non-negative integer solution exists.
              Returns [-1, -1, -1] otherwise.
    """

    # Let s = number of spiders, b = number of butterflies, d = number of dragonflies.
    # We have the following system of linear equations:
    # 1. s + b + d = total_heads
    # 2. 8s + 6b + 6d = total_legs
    # 3. 0s + 1b + 2d = total_wing_pairs  (simplified to b + 2d = total_wing_pairs)

    # From (3): b = total_wing_pairs - 2d
    # Substitute b into (1):
    # s + (total_wing_pairs - 2d) + d = total_heads
    # s + total_wing_pairs - d = total_heads
    # s = total_heads - total_wing_pairs + d

    # Substitute b and s into (2):
    # 8 * (total_heads - total_wing_pairs + d) + 6 * (total_wing_pairs - 2d) + 6d = total_legs
    # 8 * total_heads - 8 * total_wing_pairs + 8d + 6 * total_wing_pairs - 12d + 6d = total_legs
    # 8 * total_heads - 2 * total_wing_pairs + (8 - 12 + 6)d = total_legs
    # 8 * total_heads - 2 * total_wing_pairs + 2d = total_legs

    # Solve for d:
    # 2d = total_legs - 8 * total_heads + 2 * total_wing_pairs
    # d = (total_legs - 8 * total_heads + 2 * total_wing_pairs) / 2

    d_numerator = total_legs - 8 * total_heads + 2 * total_wing_pairs

    # Check if d_numerator is an even number, otherwise d cannot be an integer.
    if d_numerator % 2 != 0:
        return [-1, -1, -1]

    d = d_numerator // 2

    # Check for valid number of dragonflies
    if d < 0:
        return [-1, -1, -1]

    # Calculate b (number of butterflies)
    b = total_wing_pairs - 2 * d

    # Check for valid number of butterflies
    if b < 0:
        return [-1, -1, -1]

    # Calculate s (number of spiders)
    s = total_heads - b - d

    # Check for valid number of spiders
    if s < 0:
        return [-1, -1, -1]

    # If all values are non-negative, return the result
    return [s, b, d]
```