```python
import math

def cup_volume(top_diameter, bottom_diameter, height):
    top_radius = top_diameter / 2
    bottom_radius = bottom_diameter / 2
    volume = (math.pi * height * (top_radius**2 + top_radius * bottom_radius + bottom_radius**2)) / 3
    return round(volume, 2)
```