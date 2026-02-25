```python
from typing import List, Set, Hashable

def check_strict_superset_of_all(main_set: Set[Hashable], other_sets: List[Set[Hashable]]) -> bool:
    """
    Determines if a given main_set is a strict superset of all sets in other_sets.

    A strict superset has at least one element that does not exist in its subset.
    This means set A is a strict superset of set B if B is a subset of A and A != B.

    Args:
        main_set: The primary set (Set A in the problem description).
                  Constraints: 0 < len(main_set) < 501.
        other_sets: A list of other sets (N sets in the problem description).
                    Constraints: 0 < N < 21, and for each set s in other_sets, 0 < len(s) < 101.

    Returns:
        True if main_set is a strict superset of each set in other_sets,
        False otherwise.

    Time Complexity:
        O(sum(len(s) for s in other_sets)) on average.
        This is because checking `s.issubset(main_set)` involves iterating through 's'
        and performing hash lookups in 'main_set'. Hash lookups are O(1) on average.
        Given constraints, the maximum sum of lengths is approximately N_max * len(s)_max
        = 20 * 100 = 2000 operations.

    Space Complexity:
        O(1) auxiliary space, beyond the space taken by the input sets themselves.
    """
    # According to constraints:
    # - `main_set` is never empty (0 < len(main_set)).
    # - `other_sets` list is never empty (0 < N).
    # - Individual sets within `other_sets` are never empty (0 < len(s)).

    for other_set in other_sets:
        # For `main_set` to be a strict superset of `other_set`, two conditions must be met:
        # 1. `other_set` must be a subset of `main_set` (i.e., `main_set` contains all elements of `other_set`).
        #    This is checked by `other_set.issubset(main_set)`.
        # 2. `main_set` must contain at least one element not in `other_set`,
        #    which implies that `main_set` must have strictly more elements than `other_set`.
        #    This is checked by `len(main_set) > len(other_set)`.
        
        if not (other_set.issubset(main_set) and len(main_set) > len(other_set)):
            # If any `other_set` fails the strict superset condition,
            # `main_set` cannot be a strict superset of *all* `other_sets`.
            # We can immediately stop and return False.
            return False

    # If the loop completes, it means `main_set` successfully passed the strict superset
    # check for every set in `other_sets`.
    return True
```