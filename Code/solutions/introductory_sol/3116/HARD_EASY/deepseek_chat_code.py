```python
def cal_n_bug(heads, legs, wings_pairs):
    """
    Calculate the number of spiders, butterflies, and dragonflies given:
    - heads: total number of heads
    - legs: total number of legs  
    - wings_pairs: total number of wing pairs
    
    Returns [spiders, butterflies, dragonflies] or [-1, -1, -1] if no valid solution.
    """
    # Check for non-negative integer inputs
    if heads < 0 or legs < 0 or wings_pairs < 0:
        return [-1, -1, -1]
    
    # Let s = spiders, b = butterflies, d = dragonflies
    # Equations:
    # 1) s + b + d = heads
    # 2) 8s + 6b + 6d = legs
    # 3) 0s + 1b + 2d = wings_pairs
    
    # From equation 1: s = heads - b - d
    # Substitute into equation 2: 8(heads - b - d) + 6b + 6d = legs
    # Simplify: 8heads - 8b - 8d + 6b + 6d = legs
    # 8heads - 2b - 2d = legs
    # 2b + 2d = 8heads - legs
    # b + d = (8heads - legs) / 2
    
    # Check if (8heads - legs) is divisible by 2
    if (8 * heads - legs) % 2 != 0:
        return [-1, -1, -1]
    
    b_plus_d = (8 * heads - legs) // 2
    
    # From equation 3: b + 2d = wings_pairs
    # Subtract: (b + 2d) - (b + d) = wings_pairs - b_plus_d
    # d = wings_pairs - b_plus_d
    
    d = wings_pairs - b_plus_d
    
    # From b + d = b_plus_d, we get:
    b = b_plus_d - d
    
    # From s + b + d = heads, we get:
    s = heads - b - d
    
    # Check if all values are non-negative integers
    if s >= 0 and b >= 0 and d >= 0 and s.is_integer() and b.is_integer() and d.is_integer():
        return [int(s), int(b), int(d)]
    else:
        return [-1, -1, -1]
```