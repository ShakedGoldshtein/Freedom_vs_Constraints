```python
def cal_n_bug(heads: int, legs: int, wings: int) -> list[int, int, int]:
    """
    Calculate the number of spiders, butterflies, and dragonflies given the total heads, legs, and pairs of wings.

    Args:
        heads (int): Total number of heads.
        legs (int): Total number of legs.
        wings (int): Total number of pairs of wings.

    Returns:
        list[int, int, int]: A list containing the number of spiders, butterflies, and dragonflies.
                             Returns [-1, -1, -1] if the input does not make sense.
    """
    # Define the characteristics of each bug type
    spider_legs = 8
    butterfly_legs = 6
    dragonfly_legs = 6
    butterfly_wings = 1
    dragonfly_wings = 2

    # Iterate over possible numbers of spiders
    for spider in range(heads + 1):
        # Calculate remaining heads for butterflies and dragonflies
        remaining_heads = heads - spider
        if remaining_heads < 0:
            continue

        # Iterate over possible numbers of butterflies
        for butterfly in range(remaining_heads + 1):
            # Calculate number of dragonflies
            dragonfly = remaining_heads - butterfly
            if dragonfly < 0:
                continue

            # Calculate total legs and wings based on current distribution
            total_legs = (spider * spider_legs) + (butterfly * butterfly_legs) + (dragonfly * dragonfly_legs)
            total_wings = (butterfly * butterfly_wings) + (dragonfly * dragonfly_wings)

            # Check if the current distribution matches the given totals
            if total_legs == legs and total_wings == wings:
                return [spider, butterfly, dragonfly]

    # If no valid distribution is found, return [-1, -1, -1]
    return [-1, -1, -1]
```