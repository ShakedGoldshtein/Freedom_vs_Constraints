```python
import math

def calculate_truncated_cone_volume(top_diameter, bottom_diameter, height):
    """
    Calculate the volume of a truncated cone (frustum) using the formula:
    V = (1/3) * π * h * (R² + R*r + r²)
    where R and r are the radii of the top and bottom circles.
    """
    top_radius = top_diameter / 2
    bottom_radius = bottom_diameter / 2
    
    volume = (1/3) * math.pi * height * (
        top_radius**2 + top_radius * bottom_radius + bottom_radius**2
    )
    
    return volume

def cup_volume(top_diameter, bottom_diameter, height):
    """
    Calculate the volume of a cup with given top diameter, bottom diameter, and height.
    The cup is modeled as a truncated cone with a steady gradient from top to bottom.
    
    Args:
        top_diameter: Diameter of the top opening (positive number)
        bottom_diameter: Diameter of the bottom base (positive number)  
        height: Height of the cup (positive number)
    
    Returns:
        Volume rounded to 2 decimal places
    """
    if top_diameter <= 0 or bottom_diameter <= 0 or height <= 0:
        raise ValueError("All dimensions must be positive numbers")
    
    volume = calculate_truncated_cone_volume(top_diameter, bottom_diameter, height)
    return round(volume, 2)
```