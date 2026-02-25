```python
def cup_volume(top, bottom, height):
    pi = 3.14159265359
    r1 = top/2
    r2 = bottom/2
    # Volume of truncated cone = (π*h/3)*(r1^2 + r2^2 + r1*r2)
    volume = (pi * height / 3) * (r1**2 + r2**2 + r1*r2)
    return round(volume, 2)
```