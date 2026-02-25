```python
def solve(V: int, W: int) -> int:
    """
    Calculates the number of ways to serve V servings of Dish A and W servings of Dish B
    on V plates, such that if the i-th plate has Dish A, the (i-1)-th plate does not 
    have Dish B. This means the sequence 'BA' is forbidden.

    The constraint "if the i-th plate has serving of Dish A then (i-1)th plate should not
    have serving of Dish B" directly implies that the substring 'BA' is forbidden.
    Any arrangement that does not contain 'BA' as a substring must consist of zero or 
    more 'A's followed by zero or more 'B's. That is, all 'A's must appear before all 'B's.

    Let `num_B_used` be the number of servings of Dish B placed on the V plates.
    Then `num_A_used = V - num_B_used` must be the number of servings of Dish A.

    We have the following conditions based on available servings and total plates:
    1. `0 <= num_B_used <= V` (Cannot place more B's than total plates)
    2. `0 <= num_B_used <= W` (Cannot place more B's than available servings of B)
    3. `0 <= num_A_used <= V` (Cannot place more A's than available servings of A)
       Substituting `num_A_used = V - num_B_used` into condition 3:
       `0 <= V - num_B_used <= V`
       From `0 <= V - num_B_used` we get `num_B_used <= V`.
       From `V - num_B_used <= V` we get `-num_B_used <= 0`, which means `num_B_used >= 0`.

    Combining all conditions for `num_B_used`:
    - `num_B_used >= 0` (from derived condition 3)
    - `num_B_used <= V` (from condition 1 and derived condition 3)
    - `num_B_used <= W` (from condition 2)

    Therefore, `0 <= num_B_used <= min(V, W)`.

    For each integer value of `num_B_used` in this range, there is exactly one valid
    arrangement: `(V - num_B_used)` 'A's followed by `num_B_used` 'B's.
    The number of such integer values is `min(V, W) - 0 + 1`.
    """
    return min(V, W) + 1
```