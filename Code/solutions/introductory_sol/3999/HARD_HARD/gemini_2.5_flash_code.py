```python
import math

def cup_volume(top_diameter: float, bottom_diameter: float, height: float) -> float:
    """
    Calculates the volume of a cup (frustum of a cone) given its dimensions.

    The volume is calculated based on the formula for a frustum, assuming a
    steady gradient from the top diameter to the bottom diameter.
    All input parameters are expected to be positive numbers.

    Args:
        top_diameter: The diameter of the top opening of the cup.
        bottom_diameter: The diameter of the bottom base of the cup.
        height: The vertical height of the cup.

    Returns:
        The volume of the cup, rounded to 2 decimal places.
    """
    # Calculate radii from diameters
    # As per the problem statement, all inputs are positive numbers.
    top_radius = top_diameter / 2
    bottom_radius = bottom_diameter / 2

    # The formula for the volume of a frustum of a cone is:
    # V = (1/3) * pi * h * (R^2 + R*r + r^2)
    # where h is height, R is the radius of one base, and r is the radius of the other base.
    # The order of top_radius and bottom_radius does not affect the result
    # due to the commutative and symmetric properties of the (r1^2 + r1*r2 + r2^2) term.
    
    volume = (1/3) * math.pi * height * (
        top_radius**2 + (top_radius * bottom_radius) + bottom_radius**2
    )

    return round(volume, 2)
```