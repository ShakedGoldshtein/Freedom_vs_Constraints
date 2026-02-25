```python
def get_slope(p1, p2):
    """
    Calculates the slope of the line through two points.

    Args:
        p1 (list): The first point, an array [x1, y1].
        p2 (list): The second point, an array [x2, y2].

    Returns:
        float: The slope of the line.
        None: If the line is vertical or the same point is given twice.
    """
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    delta_x = x2 - x1
    delta_y = y2 - y1

    if delta_x == 0:
        # This covers both vertical lines (delta_y != 0)
        # and identical points (delta_y == 0)
        return None
    else:
        return delta_y / delta_x
```