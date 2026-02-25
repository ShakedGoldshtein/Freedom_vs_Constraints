```python
from typing import List

def calculate_lost_sheep(
    friday_sheep_groups: List[int],
    saturday_sheep_groups: List[int],
    total_sheep_initial: int
) -> int:
    """
    Calculates the amount of sheep lost (not returned to the farm) after the final count on Saturday.

    Sheep return in groups on Friday and Saturday. The total initial amount of sheep
    is provided. Lost sheep are those that did not return.

    Args:
        friday_sheep_groups: A list of positive integers, each representing a group of sheep
                             returned on Friday. Empty list means no sheep returned on Friday.
        saturday_sheep_groups: A list of positive integers, each representing a group of sheep
                               returned on Saturday. Empty list means no sheep returned on Saturday.
        total_sheep_initial: The total initial amount of sheep the farmer has. Must be a
                             non-negative integer.

    Returns:
        The non-negative amount of sheep lost. If the sum of returned sheep exceeds the
        initial total, it implies no sheep were lost (e.g., initial count was underestimated
        or new sheep were found), and the result is capped at 0.

    Raises:
        TypeError: If `friday_sheep_groups` or `saturday_sheep_groups` are not lists,
                   or if `total_sheep_initial` is not an integer.
        ValueError: If `total_sheep_initial` is negative.

    Time Complexity: O(F + S), where F is the number of groups in `friday_sheep_groups`
                     and S is the number of groups in `saturday_sheep_groups`. This is optimal
                     as all group sizes must be summed.
    Space Complexity: O(1), as only a few scalar variables are used for calculations,
                      independent of the input list sizes. This is optimal.
    """
    # Validate input types for robustness in a production environment.
    if not isinstance(friday_sheep_groups, list):
        raise TypeError("friday_sheep_groups must be a list.")
    if not isinstance(saturday_sheep_groups, list):
        raise TypeError("saturday_sheep_groups must be a list.")
    if not isinstance(total_sheep_initial, int):
        raise TypeError("total_sheep_initial must be an integer.")

    # Validate the value of total_sheep_initial.
    if total_sheep_initial < 0:
        raise ValueError("Total initial sheep cannot be negative.")

    # Calculate the total number of sheep returned on Friday.
    # The sum() function handles an empty list by returning 0, which is correct.
    # Per problem statement, list elements are guaranteed to be positive integers.
    sum_friday_returned = sum(friday_sheep_groups)

    # Calculate the total number of sheep returned on Saturday.
    sum_saturday_returned = sum(saturday_sheep_groups)

    # Calculate the total number of sheep that returned to the farm over the weekend.
    total_returned_sheep = sum_friday_returned + sum_saturday_returned

    # Calculate the raw difference between initial sheep and returned sheep.
    # This value could be negative if more sheep returned than initially counted.
    raw_lost_sheep_count = total_sheep_initial - total_returned_sheep

    # The amount of "lost" sheep cannot be negative. If more sheep returned
    # than initially owned, it means no sheep were lost (or perhaps the initial
    # count was an underestimate), so we cap the result at zero.
    return max(0, raw_lost_sheep_count)
```