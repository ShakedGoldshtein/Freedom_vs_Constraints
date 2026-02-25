```python
def riders(stations: list[int]) -> int:
    """
    Calculate the number of riders needed to cover all stations.

    Args:
        stations (list[int]): A list of distances between consecutive stations.

    Returns:
        int: The minimum number of riders required to cover the entire route.
    """
    total_distance = sum(stations)  # Calculate the total distance of the route
    max_distance_per_rider = 100  # Each rider can travel up to 100 miles

    # Calculate the minimum number of riders needed, rounding up if necessary
    return -(total_distance // -max_distance_per_rider)
```