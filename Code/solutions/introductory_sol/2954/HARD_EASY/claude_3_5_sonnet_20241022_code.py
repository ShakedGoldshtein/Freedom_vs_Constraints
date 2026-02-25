```python
def riders(stations):
    """
    Calculate minimum number of riders needed for Pony Express route.
    
    Args:
        stations: List of distances between consecutive stations in miles
        
    Returns:
        Integer number of riders needed
    """
    if not stations:
        return 0
        
    riders = 1
    current_distance = 0
    
    for distance in stations:
        # Check if adding next station would exceed 100 mile limit
        if current_distance + distance > 100:
            riders += 1
            current_distance = distance
        else:
            current_distance += distance
            
    return riders
```