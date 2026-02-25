```python
def solve_race(finish, distance_to_bolt, tiger_acceleration, bolt_speed):
    """
    Determines winner between Bolt and tiger in a race.
    Returns "Bolt" if Bolt wins, "Tiger" if tiger wins.
    """
    # Time for Bolt to reach finish
    bolt_time = finish / bolt_speed
    
    # For tiger to win, it needs to cover (distance_to_bolt + finish) distance
    # in less than or equal to bolt_time
    
    # Using displacement formula: S = ut + (1/2)at^2
    # where S = distance_to_bolt + finish
    # u = 0 (initial velocity)
    # a = tiger_acceleration
    # Solve quadratic equation: (1/2)at^2 = S
    
    total_distance = distance_to_bolt + finish
    tiger_time = (2 * total_distance / tiger_acceleration) ** 0.5
    
    if tiger_time <= bolt_time:
        return "Tiger"
    return "Bolt"

def solve(T, test_cases):
    """
    Solves multiple test cases.
    T: Number of test cases
    test_cases: List of (finish, distance_to_bolt, tiger_acceleration, bolt_speed)
    Returns list of results ("Bolt" or "Tiger" for each test case)
    """
    results = []
    for _ in range(T):
        finish, distance_to_bolt, tiger_acceleration, bolt_speed = test_cases[_]
        results.append(solve_race(finish, distance_to_bolt, tiger_acceleration, bolt_speed))
    return results
```