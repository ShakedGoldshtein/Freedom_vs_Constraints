```python
import math

def cup_volume(diameter_top, diameter_bottom, height):
    """
    Calculates the volume of a frustum (truncated cone) given its top diameter,
    bottom diameter, and height. The volume is returned rounded to 2 decimal places.
    """
    
    # The formula for the volume of a frustum is V = (1/3) * pi * h * (R_top^2 + R_top*R_bottom + R_bottom^2)
    # where R_top and R_bottom are the radii of the top and bottom bases, respectively.
    # Given diameters, we can convert to radii: R = D / 2
    # Substituting D/2 for R in the formula:
    # V = (1/3) * pi * h * ((D_top/2)^2 + (D_top/2)*(D_bottom/2) + (D_bottom/2)^2)
    # V = (1/3) * pi * h * (D_top^2/4 + (D_top*D_bottom)/4 + D_bottom^2/4)
    # V = (1/3) * pi * h * (1/4) * (D_top^2 + D_top*D_bottom + D_bottom^2)
    # V = (math.pi / 12) * height * (diameter_top^2 + diameter_top*diameter_bottom + diameter_bottom^2)

    sum_of_squares_and_products = diameter_top**2 + diameter_top * diameter_bottom + diameter_bottom**2
    volume = (math.pi / 12) * height * sum_of_squares_and_products
    
    return round(volume, 2)
```