```python
def calculate_min_fatigue(n: int, a: int, b: int, x_coords: list[int]) -> int:
    """
    Calculates the minimum possible total increase of fatigue level to visit all towns.

    You start at town 1 and need to visit all other towns (2 through N).
    You can either walk or teleport between adjacent towns.
    Walking increases fatigue by 'A' per unit distance.
    Teleporting increases fatigue by 'B', regardless of distance.

    The problem is solved by iterating through each adjacent pair of towns
    and deciding the minimum fatigue for that specific segment (either walk or teleport).
    Since the decisions for each segment are independent and contribute additively to
    the total fatigue, a greedy approach yields the optimal solution.

    Args:
        n: The total number of towns. Must be an integer such that 2 <= N <= 10^5.
        a: The fatigue increase per unit distance for walking. Must be an integer
           such that 1 <= A <= 10^9.
        b: The fatigue increase for teleporting. Must be an integer
           such that 1 <= B <= 10^9.
        x_coords: A list of N integers representing the coordinates of the towns.
                  The towns are numbered 1 through N, and their coordinates are
                  given in order, i.e., X_1, X_2, ..., X_N.
                  For all i (1 <= i <= N-1), X_i < X_{i+1}, and 1 <= X_i <= 10^9.

    Returns:
        The minimum possible total increase of your fatigue level, as an integer.
        This value can be large, fitting within Python's arbitrary-precision integers.
    """
    total_fatigue = 0

    # Iterate through all N-1 segments between adjacent towns.
    # For towns 1 to N, there are segments (1,2), (2,3), ..., (N-1,N).
    # The list x_coords is 0-indexed, so x_coords[i] corresponds to town i+1.
    for i in range(n - 1):
        # Calculate the distance between the current town (x_coords[i])
        # and the next town (x_coords[i+1]).
        # The coordinates are strictly increasing, so distance will always be positive.
        distance = x_coords[i+1] - x_coords[i]

        # Calculate the fatigue incurred if choosing to walk this distance.
        # Fatigue is distance multiplied by A.
        fatigue_walk = distance * a

        # Compare walking fatigue with teleporting fatigue (which is a fixed cost B).
        # Add the minimum of these two options to the total fatigue.
        total_fatigue += min(fatigue_walk, b)

    return total_fatigue
```