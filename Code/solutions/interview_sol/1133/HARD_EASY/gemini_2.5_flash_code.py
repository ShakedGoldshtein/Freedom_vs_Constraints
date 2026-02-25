```python
import math
from typing import List, Tuple

def _calculate_gcd_of_list(numbers: List[int]) -> int:
    """
    Calculates the Greatest Common Divisor (GCD) of a list of positive integers.

    Args:
        numbers: A list of positive integers. Must not be empty.
                 (Guaranteed by problem constraints: 1 <= N).

    Returns:
        The GCD of all numbers in the list.
    """
    # According to problem constraints, 'numbers' will always contain at least one
    # positive integer (1 <= N, 1 <= Ai).
    
    result_gcd = numbers[0]
    for i in range(1, len(numbers)):
        result_gcd = math.gcd(result_gcd, numbers[i])
        # Optimization: If the GCD becomes 1 at any point, it cannot get smaller.
        # Thus, the GCD of the entire list must be 1. We can return early.
        if result_gcd == 1: 
            return 1
    return result_gcd

def solve(n: int, a_lengths: List[int]) -> Tuple[int, int]:
    """
    Solves Shivam's wire buying problem to minimize total expenditure.

    The problem requires choosing a single integer length for all purchased wire pieces.
    Each required wire length (A_i) must be a perfect multiple of the chosen piece length.
    The goal is to find the optimal chosen piece length and the corresponding
    minimum total cost (total number of pieces).

    To minimize the total number of wire pieces (and thus total cost), Shivam must
    choose the largest possible length 'L' such that every required length A_i is
    a multiple of 'L'. This 'L' is the Greatest Common Divisor (GCD) of all A_i.

    Args:
        n: The number of connections. This parameter is included to match the
           problem's input specification, but its value is equivalent to len(a_lengths).
           Constraints: 1 <= n <= 10^5.
        a_lengths: A list of integers representing the lengths of wires
                   required for each connection.
                   Constraints: 1 <= a_lengths[i] <= 10^5 for each element.

    Returns:
        A tuple containing two integers:
        - The optimal chosen length for each wire piece.
        - The corresponding minimum total cost (total number of purchased pieces).
    """
    # Step 1: Calculate the Greatest Common Divisor (GCD) of all required lengths.
    # This GCD value represents the largest possible length for individual wire
    # pieces that can be used to construct all required_lengths without waste.
    optimal_piece_length = _calculate_gcd_of_list(a_lengths)

    # Step 2: Calculate the total number of wire pieces needed for this optimal length.
    # For each required length A_i, the number of pieces needed is A_i / optimal_piece_length.
    # The total cost is the sum of these individual piece requirements.
    # Integer division (//) is used because 'optimal_piece_length' is guaranteed
    # to perfectly divide each 'a_length' (by definition of GCD).
    total_cost = sum(length // optimal_piece_length for length in a_lengths)

    return optimal_piece_length, total_cost
```