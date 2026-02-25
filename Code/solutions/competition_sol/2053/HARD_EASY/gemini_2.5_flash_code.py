```python
import math

def calculate_min_sweets(n: int, m: int, b: list[int], g: list[int]) -> int:
    """
    Calculates the minimum total number of sweets that boys could present
    to satisfy all given conditions.

    Args:
        n: The number of boys.
        m: The number of girls.
        b: A list of n integers, where b[i] is the minimal number of sweets
           the (i+1)-th boy presented to some girl.
        g: A list of m integers, where g[j] is the maximal number of sweets
           the (j+1)-th girl received from some boy.

    Returns:
        The minimal total number of sweets if a valid distribution is possible,
        otherwise -1.
    """
    # Sort b and g lists to easily access min/max values.
    # Sorting is O(N log N) + O(M log M)
    b_sorted = sorted(b)
    g_sorted = sorted(g)

    # Core impossibility check: For any a_i,j, we must have b_i <= a_i,j <= g_j.
    # This implies that max(b_i) must be less than or equal to min(g_j).
    # If this is not satisfied, it's impossible.
    if b_sorted[-1] > g_sorted[0]:
        return -1

    # Base sum: Initialize total_sweets by assuming each boy i gives b_i sweets
    # to all m girls. This satisfies the 'min sweets for boy i' condition.
    # sum(b) is O(N).
    total_sweets = sum(b) * m

    # Adjust sum to satisfy 'max sweets for girl j' conditions.
    # For each girl j, the maximum sweets received must be g_j.
    # With a_i,j = b_i, the max received by any girl is max(b_k).
    # If g_j > max(b_k), we must increase at least one a_k,j to g_j.
    # To minimize the total sum, we should increment the smallest possible value.
    # This is done by picking a boy k with b_k = max(b) and changing a_k,j from b_k to g_j.
    # The cost added for this is (g_j - b_k).
    # This loop is O(M).
    max_b = b_sorted[-1]
    for g_val in g:
        if g_val > max_b:
            total_sweets += (g_val - max_b)

    # Re-check the 'min sweets for boy i' condition for the boy(s) with max_b.
    # If g_sorted[0] > max_b (i.e., min(g_j) > max(b_i)), it implies that
    # all g_j values are strictly greater than max_b.
    # In the current construction, for the boy 'i_max' who has b_i = max_b,
    # all his a_i_max,j values would have been set to g_j (since all g_j > max_b).
    # This makes min(a_i_max,j) = min(g_j) = g_sorted[0].
    # But we need min(a_i_max,j) = b_i_max = max_b.
    # Since g_sorted[0] > max_b, this condition is violated.
    # To fix this, for at least one girl j_0, the boy i_max must give exactly b_i_max sweets.
    # But for this j_0, max_i(a_i,j_0) must still be g_j_0.
    # This means some other boy must provide g_j_0 sweets to girl j_0.
    # To minimize the additional cost, we pick the boy with the second largest b value (b_sorted[-2]).
    # For one girl j_0, instead of increasing a_i_max,j_0 by (g_j_0 - max_b),
    # we increase a_i_second_max,j_0 by (g_j_0 - b_sorted[-2]).
    # The net additional cost is (g_j_0 - b_sorted[-2]) - (g_j_0 - max_b) = max_b - b_sorted[-2].
    # This additional cost is incurred once.
    if g_sorted[0] > max_b:
        # N is guaranteed to be >= 2, so b_sorted[-2] always exists.
        total_sweets += (max_b - b_sorted[-2])

    return total_sweets

```