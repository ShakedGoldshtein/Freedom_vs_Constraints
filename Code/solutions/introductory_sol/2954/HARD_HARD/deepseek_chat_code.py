```python
def riders(stations):
    """
    Calculate the number of riders needed for the Pony Express route.
    
    Args:
        stations: List of distances between consecutive stations in miles
        
    Returns:
        Number of riders required to cover the entire route
    """
    if not stations:
        return 0
    
    riders_count = 1
    current_distance = 0
    
    for distance in stations:
        if distance > 100:
            return 0
        
        current_distance += distance
        
        if current_distance > 100:
            riders_count += 1
            current_distance = distance
    
    return riders_count
```