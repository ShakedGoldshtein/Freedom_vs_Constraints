```python
import math

def calculate_single_case_probability(S: int, N: int, M: int, K: int) -> float:
    """
    Calculates the probability that Alice will enjoy the trip given that she goes on the trip.

    Alice enjoys the trip if at least K of her friends (excluding herself) are also selected.

    Args:
        S: Total number of students in the class.
        N: Number of students to be picked for the trip.
        M: Total students in Alice's friend circle (including Alice).
        K: Minimum number of Alice's friends (excluding Alice) required for her to enjoy.

    Returns:
        The probability as a float.
    """
    
    # Adjust parameters assuming Alice is already selected for the trip.
    # Total students remaining in the pool (excluding Alice).
    remaining_class_students = S - 1
    # Number of spots remaining to be filled on the trip (excluding Alice's spot).
    remaining_trip_spots = N - 1
    
    # Alice's friends available for selection (excluding Alice).
    alice_friends_excluding_alice = M - 1
    # Non-friends available for selection (excluding Alice).
    non_friends_excluding_alice = S - M
    
    # Calculate the total number of ways to choose the remaining students for the trip.
    # This is C(remaining_class_students, remaining_trip_spots).
    # Given constraints (1 <= N <= S), remaining_trip_spots (N-1) will always be
    # between 0 and remaining_class_students (S-1) inclusive.
    # Thus, math.comb will return a value >= 1.
    total_ways_to_fill_spots = math.comb(remaining_class_students, remaining_trip_spots)
    
    # Initialize sum for favorable combinations.
    favorable_ways_sum = 0
    
    # Determine the valid range for 'num_friends_chosen', the number of Alice's friends selected.
    # 1. 'num_friends_chosen' must be at least K (the minimum required).
    # 2. 'num_friends_chosen' cannot exceed the total number of Alice's friends available (M-1).
    # 3. 'num_friends_chosen' cannot exceed the remaining spots on the trip (N-1).
    # 4. The number of non-friends chosen is (remaining_trip_spots - num_friends_chosen).
    #    This must not exceed the total number of non-friends available (S-M).
    #    So, (remaining_trip_spots - num_friends_chosen) <= (S-M)
    #    This implies num_friends_chosen >= remaining_trip_spots - (S-M).
    
    lower_bound_friends = max(K, remaining_trip_spots - non_friends_excluding_alice)
    upper_bound_friends = min(alice_friends_excluding_alice, remaining_trip_spots)
    
    # Iterate through all possible numbers of Alice's friends that can be chosen
    # to satisfy the conditions.
    if lower_bound_friends <= upper_bound_friends:
        for num_friends_chosen in range(lower_bound_friends, upper_bound_friends + 1):
            num_non_friends_chosen = remaining_trip_spots - num_friends_chosen
            
            # Calculate ways to choose 'num_friends_chosen' from Alice's friends.
            # math.comb returns 0 if num_friends_chosen is out of bounds, which is handled
            # by the range calculation for lower_bound_friends and upper_bound_friends.
            ways_friends = math.comb(alice_friends_excluding_alice, num_friends_chosen)
            
            # Calculate ways to choose 'num_non_friends_chosen' from non-friends.
            ways_non_friends = math.comb(non_friends_excluding_alice, num_non_friends_chosen)
            
            favorable_ways_sum += ways_friends * ways_non_friends
            
    # The probability is the ratio of favorable ways to total ways.
    # total_ways_to_fill_spots is guaranteed to be >= 1 by constraints.
    return float(favorable_ways_sum) / total_ways_to_fill_spots


def calculate_field_trip_probabilities(test_cases: list[tuple[int, int, int, int]]) -> list[float]:
    """
    Calculates the probability for multiple field trip scenarios.

    This function processes a list of test cases, each defining a field trip scenario,
    and returns a list of probabilities.

    Args:
        test_cases: A list of tuples, where each tuple contains
                    (S, N, M, K) for a single test case:
                    S: Total students in the class.
                    N: Number of students picked for the trip.
                    M: Alice's friend circle size (including Alice).
                    K: Minimum friends (excluding Alice) for Alice to enjoy the trip.

    Returns:
        A list of probabilities (floats), one for each test case,
        in the same order as the input test cases.
    """
    results = []
    for S, N, M, K in test_cases:
        probability = calculate_single_case_probability(S, N, M, K)
        results.append(probability)
    return results
```