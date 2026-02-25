```python
def _count_valid_arrangements(num_plates: int, available_a: int, available_b: int) -> int:
    """
    Calculates the number of ways to arrange dishes A and B on a given number of plates
    adhering to specific constraints.

    The problem states that if plate 'i' has Dish A, then plate 'i-1' must not have Dish B.
    This implies that no 'BA' sequence is allowed in the arrangement.
    Consequently, any valid arrangement must be of the form 'A...A B...B',
    where 'k' servings of Dish A are followed by 'm' servings of Dish B.
    All 'num_plates' must be filled, so k + m = num_plates.
    The number of A's used (k) must not exceed 'available_a'.
    The number of B's used (m) must not exceed 'available_b'.

    Args:
        num_plates: The total number of plates to be filled.
        available_a: The maximum number of Dish A servings that can be used.
        available_b: The maximum number of Dish B servings that can be used.

    Returns:
        The number of distinct valid ways to serve the dishes.
    """
    # Let 'k' be the number of Dish A servings used and 'm' be the number of Dish B servings used.
    # 1. All 'num_plates' must be filled: k + m = num_plates
    # 2. Servings used cannot exceed what's available:
    #    0 <= k <= available_a
    #    0 <= m <= available_b

    # From (1), we can express 'm' in terms of 'k': m = num_plates - k.
    # Substitute this into the inequalities for 'm':
    #    0 <= num_plates - k      =>  k <= num_plates
    #    num_plates - k <= available_b  =>  k >= num_plates - available_b

    # Combining all conditions on 'k':
    # The lower bound for 'k' is the maximum of 0 (cannot use negative A's)
    # and (num_plates - available_b) (to ensure enough B's are available for remaining plates).
    min_k_inclusive = max(0, num_plates - available_b)

    # The upper bound for 'k' is the minimum of 'num_plates' (cannot use more A's than plates)
    # and 'available_a' (cannot use more A's than available).
    max_k_inclusive = min(num_plates, available_a)

    # If the calculated lower bound for 'k' is greater than its upper bound,
    # then no valid integer 'k' exists, meaning there are no valid arrangements.
    if min_k_inclusive > max_k_inclusive:
        return 0

    # Otherwise, the number of valid values for 'k' (and thus 'm') is the count
    # of integers in the range [min_k_inclusive, max_k_inclusive].
    # This count is (max_k_inclusive - min_k_inclusive + 1).
    return max_k_inclusive - min_k_inclusive + 1


def solve(V: int, W: int) -> int:
    """
    Calculates the number of ways Tejas can serve dishes for the Clash Team dinner party.

    V serves a dual purpose: it represents both the total number of plates available
    and the total number of servings of Dish A available.
    W represents the total number of servings of Dish B available.

    The core constraint is that if the i-th plate has Dish A, then the (i-1)-th
    plate must not have Dish B (i.e., no 'BA' sequence is allowed in the arrangement).
    All V plates must be filled.

    Args:
        V: An integer representing the total number of plates AND the quantity of Dish A servings.
        W: An integer representing the quantity of Dish B servings.

    Returns:
        An integer representing the total number of valid ways Tejas can serve the dishes.
    """
    # Delegate the calculation to the helper function, passing V for num_plates,
    # V for available_a, and W for available_b as per the problem's interpretation.
    return _count_valid_arrangements(num_plates=V, available_a=V, available_b=W)
```