```python
def calculate_min_sweets(n: int, m: int, b: list[int], g: list[int]) -> int:
    """
    Calculates the minimum total number of sweets that boys could present,
    satisfying the given conditions.

    Args:
        n: The number of boys.
        m: The number of girls.
        b: A list of n integers, where b[i] is the minimal number of sweets
           the i-th boy presented to some girl.
        g: A list of m integers, where g[j] is the maximal number of sweets
           the j-th girl received from some boy.

    Returns:
        The minimal total number of sweets, or -1 if the situation is impossible.
    """

    # Sort b and g arrays to easily access min/max values.
    # b_sorted[0] is the smallest b_i, b_sorted[n-1] is the largest b_i.
    # g_sorted[0] is the smallest g_j, g_sorted[m-1] is the largest g_j.
    b.sort()
    g.sort()

    # Initial impossibility check:
    # For any a_i,j, it must hold that b_i <= a_i,j <= g_j.
    # This implies that for any boy i and any girl j, b_i <= g_j.
    # Therefore, the maximum b_i must be less than or equal to the minimum g_j.
    # If max(b) > min(g), it's impossible.
    if b[n - 1] > g[0]:
        return -1

    # Calculate the base total sweets:
    # Each boy i must give at least b_i sweets to each of the m girls.
    # We start by assuming each a_i,j = b_i.
    # This satisfies a_i,j >= b_i and min_j(a_i,j) = b_i for all boys.
    total_sweets = sum(b) * m

    # Adjust for girl requirements (max_i(a_i,j) = g_j):
    # With a_i,j = b_i, the maximum sweets received by any girl j from any boy is max(b) = b[n-1].
    # If g_j (the required maximum for girl j) is greater than b[n-1],
    # we must increase at least one a_k,j to g_j.
    # To minimize the sum, for each such g_j, we choose the boy with the largest b_i (boy b[n-1])
    # to contribute the additional sweets. So, a_(n-1),j is set to g_j.
    # This adds (g_j - b[n-1]) to the total sweets for each such girl j.
    for val_g in g:
        if val_g > b[n - 1]:
            total_sweets += (val_g - b[n - 1])

    # Handle a special case for boy b[n-1]'s minimum condition:
    # After the adjustments in the previous step, all boys i < n-1 still have a_i,j = b_i for all j,
    # so their min_j(a_i,j) = b_i condition is met.
    # All girls j now satisfy max_i(a_i,j) = g_j.
    # The only remaining condition to verify is min_j(a_(n-1),j) = b[n-1].
    #
    # Current construction for boy b[n-1] (boy with the largest b value):
    # - If g_j > b[n-1], we set a_(n-1),j = g_j.
    # - If g_j = b[n-1], we effectively keep a_(n-1),j = b[n-1].
    #
    # If there is at least one girl j_0 such that g_j_0 = b[n-1],
    # then a_(n-1),j_0 would remain b[n-1], satisfying min_j(a_(n-1),j) = b[n-1].
    #
    # The problem arises if ALL g_j values are strictly greater than b[n-1].
    # This implies b[n-1] < g[0]. In this scenario, for boy b[n-1], we would have set
    # a_(n-1),j = g_j for all j. Consequently, min_j(a_(n-1),j) would be min(g_j) = g[0].
    # Since g[0] > b[n-1], this violates boy b[n-1]'s minimum condition.
    #
    # To fix this:
    # We need to ensure at least one a_(n-1),j_0 = b[n-1].
    # We choose an arbitrary girl (say, g[0]) and set a_(n-1),0 = b[n-1].
    # This change means we "undo" the increment (g[0] - b[n-1]) that was added for g[0]
    # in the previous step (as a_(n-1),0 is now b[n-1] instead of g[0]).
    #
    # However, now max_i(a_i,0) for girl g[0] becomes b[n-1] (since a_(n-1),0 is b[n-1]
    # and all other a_i,0 are b_i <= b[n-1]). But it must be g[0].
    # So, another boy must provide g[0] sweets to girl 0.
    # To minimize the sum, we pick the boy with the second largest b value (boy b[n-2]).
    # We set a_(n-2),0 = g[0] (instead of b[n-2]). This adds (g[0] - b[n-2]) to the sum.
    #
    # The net change to total_sweets for this adjustment (for girl 0):
    #   - (g[0] - b[n-1])  (remove previous increment for a_(n-1),0)
    #   + (g[0] - b[n-2])  (add new increment for a_(n-2),0)
    # Net change = b[n-1] - b[n-2].
    # This change is applied only if b[n-1] < g[0].
    # This strategy also works for n=2 (where b[n-2] is b[0]).
    if b[n - 1] < g[0]:
        total_sweets += (b[n - 1] - b[n - 2])

    return total_sweets
```