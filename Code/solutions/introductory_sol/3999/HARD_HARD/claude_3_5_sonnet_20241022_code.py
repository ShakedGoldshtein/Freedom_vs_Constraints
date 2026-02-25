```python
def cup_volume(top_diameter, bottom_diameter, height):
    """
    Calculate volume of a truncated cone (cup) given top diameter, bottom diameter and height.
    Returns volume rounded to 2 decimal places.
    
    Args:
        top_diameter (float): Diameter of the top of the cup
        bottom_diameter (float): Diameter of the bottom of the cup 
        height (float): Height of the cup
        
    Returns:
        float: Volume of the cup rounded to 2 decimal places
    """
    import math
    
    # Calculate radius for top and bottom
    r1 = top_diameter / 2
    r2 = bottom_diameter / 2
    
    # Use truncated cone volume formula: V = (πh/3)(r1² + r2² + r1*r2)
    volume = (math.pi * height / 3) * (r1**2 + r2**2 + r1*r2)
    
    return round(volume, 2)
```