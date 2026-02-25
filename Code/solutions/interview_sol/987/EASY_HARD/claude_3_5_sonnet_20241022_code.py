```python
def solve_race(finish, distance_to_bolt, tiger_acceleration, bolt_speed):
    # Time taken by Bolt to reach finish
    bolt_time = finish / bolt_speed
    
    # For tiger to win, it needs to cover (distance_to_bolt + finish) distance
    # Using quadratic formula: 0.5 * a * t^2 = d
    # where a = acceleration, t = time, d = total distance
    total_distance = distance_to_bolt + finish
    tiger_time = (2 * total_distance / tiger_acceleration) ** 0.5
    
    if tiger_time <= bolt_time:
        return "Tiger"
    return "Bolt"

def solve(T, races):
    result = []
    for _ in range(T):
        finish, distance_to_bolt, tiger_acceleration, bolt_speed = races[_]
        result.append(solve_race(finish, distance_to_bolt, tiger_acceleration, bolt_speed))
    return result
```