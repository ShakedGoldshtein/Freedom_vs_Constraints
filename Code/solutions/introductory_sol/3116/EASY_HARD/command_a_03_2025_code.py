```python
def cal_n_bug(heads: int, legs: int, wings: int) -> list[int, int, int]:
    """
    Calculate the number of spiders, butterflies, and dragonflies based on the given heads, legs, and pairs of wings.

    Args:
        heads (int): Total number of heads.
        legs (int): Total number of legs.
        wings (int): Total number of pairs of wings.

    Returns:
        list[int, int, int]: A list containing the number of spiders, butterflies, and dragonflies. 
                             Returns [-1, -1, -1] if the input does not make sense.
    """
    # Iterate over possible numbers of spiders (0 to heads)
    for spiders in range(heads + 1):
        # Calculate the remaining heads for butterflies and dragonflies
        remaining_heads = heads - spiders
        
        # Iterate over possible numbers of butterflies (0 to remaining_heads)
        for butterflies in range(remaining_heads + 1):
            # Calculate the number of dragonflies
            dragonflies = remaining_heads - butterflies
            
            # Calculate total legs and wings based on the current combination
            total_legs = spiders * 8 + butterflies * 6 + dragonflies * 6
            total_wings = butterflies * 1 + dragonflies * 2
            
            # Check if the current combination matches the given legs and wings
            if total_legs == legs and total_wings == wings:
                return [spiders, butterflies, dragonflies]
    
    # If no valid combination is found, return [-1, -1, -1]
    return [-1, -1, -1]
```