```python
def get_slope(point1, point2):
    """
    Calculate the slope of the line through two points. 
    Returns None if the line is vertical or the points are the same.
    """
    
    # Check if points are the same
    if point1 == point2: 
        return None
    
    # Check if line is vertical
    if point1[0] == point2[0]: 
        return None
    
    # Calculate slope
    slope = (point2[1] - point1[1]) / (point2[0] - point1[0]) 

    return slope
```