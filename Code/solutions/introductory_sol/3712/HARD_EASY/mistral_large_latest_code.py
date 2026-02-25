```python
def get_slope(point1: list[float], point2: list[float]) -> float | None:
    """
    Calculate the slope of the line through two points.

    Args:
        point1: First point as [x, y] coordinates.
        point2: Second point as [x, y] coordinates.

    Returns:
        The slope of the line through the points, or None if the line is vertical
        or if the points are identical.
    """
    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2:
        return None
    if y1 == y2:
        return 0.0

    return (y2 - y1) / (x2 - x1)
```