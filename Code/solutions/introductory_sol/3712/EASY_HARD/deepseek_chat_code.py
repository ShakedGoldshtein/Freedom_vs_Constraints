```python
def get_slope(point1, point2):
    if point1[0] == point2[0]:
        return None
    return (point2[1] - point1[1]) / (point2[0] - point1[0])
```