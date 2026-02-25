```python
def riders(stations: list[int]) -> int:
    """
    Calculate the number of riders needed to cover the Pony Express route.

    Args:
        stations (list[int]): A list of distances (miles) between consecutive stations.

    Returns:
        int: The minimum number of riders required to cover the entire route.
             Each rider can travel up to 100 miles.
    """
    if not stations:
        return 0

    total_distance = sum(stations)
    max_rider_distance = 100
    riders_needed = 1
    current_distance = 0

    for distance in stations:
        if current_distance + distance > max_rider_distance:
            riders_needed += 1
            current_distance = distance
        else:
            current_distance += distance

    return riders_needed
```