```python
import math

def cup_volume(d1, d2, h):
    r1 = d1 / 2
    r2 = d2 / 2
    volume = (1/3) * math.pi * h * (r1**2 + r1*r2 + r2**2)
    return round(volume, 2)
```