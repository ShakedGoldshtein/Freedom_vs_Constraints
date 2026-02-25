```python
import math

def solve(S: int, N: int, M: int, K: int) -> float:
    """
    Calculates the probability that Alice will enjoy the trip, given that she goes on the trip.

    Args:
        S (int): Total number of students in the class.
        N (int): Number of students going on the trip.
        M (int): Number of students in Alice's friend circle (including Alice).
        K (int): Minimum number of Alice's friends (excluding Alice herself)
                 that must accompany her for her to enjoy the trip.

    Returns:
        float: The probability that Alice enjoys the trip.
    """

    # If Alice goes on the trip, there are N-1 remaining spots to fill
    # from the S-1 remaining students (total students minus Alice).
    # This is the total number of ways to pick the rest of the trip attendees,
    # given Alice is already chosen.
    total_ways_to_fill_remaining_spots = math.comb(S - 1, N - 1)

    # If it's impossible to pick N-1 students from S-1 (e.g., N-1 > S-1),
    # or if there are no students available (S-1 < 0), total_ways_to_fill_remaining_spots will be 0.
    # Given constraints (1 <= N <= S), S-1 >= N-1, and S-1 >= 0. So this will always be >= 1.
    # However, if N=0 (not allowed by constraints) or similar edge cases lead to 0,
    # it implies an impossible scenario, and probability should be 0.
    if total_ways_to_fill_remaining_spots == 0:
        return 0.0

    favorable_ways = 0

    # We need to choose 'j' friends from Alice's (M-1) friends
    # and (N-1 - j) non-friends from the (S-M) non-friends.

    # Minimum number of friends (excluding Alice) required to be picked is K.
    min_friends_to_pick = K

    # Maximum number of friends (excluding Alice) that can be picked is limited by:
    # 1. The total number of Alice's friends (excluding Alice): M-1
    # 2. The number of remaining spots on the trip: N-1
    max_friends_to_pick = min(M - 1, N - 1)

    # Iterate through all possible numbers of friends 'j' (from M-1) that can be picked.
    # The range for 'j' goes from max(0, min_friends_to_pick) up to max_friends_to_pick.
    # math.comb(n, k) returns 0 if k < 0 or k > n, simplifying boundary checks.
    for j in range(min_friends_to_pick, max_friends_to_pick + 1):
        # Number of non-friends that must be picked
        num_non_friends_to_pick = (N - 1) - j

        # Calculate ways to choose 'j' friends from M-1 available friends
        ways_to_pick_friends = math.comb(M - 1, j)

        # Calculate ways to choose 'num_non_friends_to_pick' non-friends from S-M available non-friends
        ways_to_pick_non_friends = math.comb(S - M, num_non_friends_to_pick)

        favorable_ways += ways_to_pick_friends * ways_to_pick_non_friends

    if favorable_ways == 0:
        return 0.0
    
    probability = favorable_ways / total_ways_to_fill_remaining_spots
    return probability
```