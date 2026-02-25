```python
MAX_RIDER_DISTANCE = 100

def riders(stations: list[int]) -> int:
    """
    Calculates the minimum number of riders necessary to transport mail along a route.

    Each rider travels as far as they can, but never more than a fixed maximum distance
    (100 miles). A rider must switch at a station. If a single segment between stations
    is greater than this maximum distance, it's impossible to complete the route.

    Args:
        stations: A list of integers representing distances (in miles) from one station
                  to the next along the Pony Express route. Each distance must be a
                  non-negative integer.

    Returns:
        The number of riders required to cover the entire route.

    Raises:
        ValueError: If any element in `stations` is not a non-negative integer, or
                    if any single station-to-station segment distance exceeds
                    the maximum rider travel distance (100 miles), as it's impossible
                    for a rider to traverse such a segment.
    """
    if not stations:
        return 0

    riders_count = 1
    current_rider_distance = 0

    for segment_distance in stations:
        # Validate segment distance type and value
        if not isinstance(segment_distance, int) or segment_distance < 0:
            raise ValueError("Station distances must be non-negative integers.")
        
        # Check if a single segment is too long for any rider
        if segment_distance > MAX_RIDER_DISTANCE:
            raise ValueError(
                f"Individual station segment ({segment_distance} miles) "
                f"exceeds rider's maximum travel distance of {MAX_RIDER_DISTANCE} miles. "
                "The route cannot be completed under these conditions."
            )

        # Attempt to add the current segment to the current rider's journey
        if current_rider_distance + segment_distance <= MAX_RIDER_DISTANCE:
            current_rider_distance += segment_distance
        else:
            # The current rider cannot take this segment without exceeding the limit.
            # A new rider must start from the current station.
            riders_count += 1
            current_rider_distance = segment_distance
            
    return riders_count
```