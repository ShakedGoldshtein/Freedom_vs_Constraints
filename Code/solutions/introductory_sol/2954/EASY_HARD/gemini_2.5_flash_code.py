```python
def riders(stations):
    if not stations:
        return 0

    num_riders = 1
    current_rider_distance = 0

    for distance_to_next_station in stations:
        if current_rider_distance + distance_to_next_station > 100:
            # The current rider cannot cover this leg without exceeding 100 miles.
            # A new rider is needed, starting fresh from the current station.
            num_riders += 1
            current_rider_distance = distance_to_next_station
        else:
            # The current rider can cover this leg.
            current_rider_distance += distance_to_next_station
            
    return num_riders
```