```python
def get_slope(p1, p2):
    """
    Calculate slope of line through two points.
    Args:
        p1: List of [x1,y1] coordinates for point 1
        p2: List of [x2,y2] coordinates for point 2
    Returns:
        float: slope of line, or None if vertical line or same points
    """
    if not p1 or not p2:
        return None
        
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    
    if x1 == x2:
        if y1 == y2:
            return None
        return None
        
    return (y2 - y1) / (x2 - x1)
```