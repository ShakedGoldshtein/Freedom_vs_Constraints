```python
def cal_n_bug(n_heads, n_legs, n_pairs_wings):
    """
    Calculate number of spiders, butterflies and dragonflies given total heads, legs and wing pairs.
    Returns [spiders, butterflies, dragonflies] if a valid solution exists, [-1,-1,-1] otherwise.
    
    Args:
        n_heads: Total number of heads (integer)
        n_legs: Total number of legs (integer) 
        n_pairs_wings: Total number of wing pairs (integer)
        
    Returns:
        List of [spiders, butterflies, dragonflies] or [-1,-1,-1] if no valid solution
    """
    
    # Check for negative or non-integer inputs
    if not isinstance(n_heads, int) or not isinstance(n_legs, int) or not isinstance(n_pairs_wings, int):
        return [-1, -1, -1]
    
    # Try all possible combinations given number of heads
    for spiders in range(n_heads + 1):
        for butterflies in range(n_heads + 1 - spiders):
            dragonflies = n_heads - spiders - butterflies
            
            # Check if this combination matches legs and wings
            total_legs = 8*spiders + 6*butterflies + 6*dragonflies
            total_wings = butterflies + 2*dragonflies
            
            if (total_legs == n_legs and 
                total_wings == n_pairs_wings and
                spiders >= 0 and butterflies >= 0 and dragonflies >= 0):
                return [spiders, butterflies, dragonflies]
                
    return [-1, -1, -1]
```