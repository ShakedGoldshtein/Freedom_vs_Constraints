```python
import math

def cup_volume(top_diameter: float, bottom_diameter: float, height: float) -> float:
    """
    Calculate the volume of a cup with a steady gradient from top to bottom.

    Args:
        top_diameter: Diameter of the top of the cup (must be positive).
        bottom_diameter: Diameter of the bottom of the cup (must be positive).
        height: Height of the cup (must be positive).

    Returns:
        Volume of the cup rounded to 2 decimal places.
    """
    top_radius = top_diameter / 2.0
    bottom_radius = bottom_diameter / 2.0

    # Volume of a frustum of a cone: (1/3) * π * h * (r1² + r1*r2 + r2²)
    volume = (math.pi * height / 3.0) * (
        top_radius**2 +
        top_radius * bottom_radius +
        bottom_radius**2
    )

    return round(volume, 2)
```