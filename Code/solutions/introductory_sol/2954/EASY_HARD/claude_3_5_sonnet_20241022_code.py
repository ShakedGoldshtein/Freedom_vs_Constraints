```python
def riders(stations):
    if not stations:
        return 0
        
    riders = 1
    current_distance = 0
    
    for distance in stations:
        if current_distance + distance > 100:
            riders += 1
            current_distance = distance
        else:
            current_distance += distance
            
    return riders
```