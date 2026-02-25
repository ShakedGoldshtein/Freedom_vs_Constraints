```python
def find_max_nice_staircases(total_cells_x: int) -> int:
    """
    Calculates the maximum number of different nice staircases that can be built
    using no more than `total_cells_x` cells in total.

    A staircase with 'n' stairs is made of 'n' columns, where the i-th column
    is 'i' cells high. The total cells for such a staircase is n * (n + 1) / 2.
    A staircase is considered 'nice' if 'n' is of the form 2^k - 1 for k >= 1.
    To maximize the number of different nice staircases using a limited budget,
    we employ a greedy strategy: always build the cheapest available nice
    staircase first. The costs of nice staircases (n=1, n=3, n=7, ...)
    increase rapidly, making this greedy choice optimal.

    Args:
        total_cells_x: The total number of cells available for building.
                       Guaranteed to be 1 <= total_cells_x <= 10^18.

    Returns:
        The maximum number of different nice staircases that can be built.
    """
    count = 0
    # 'n_stairs' represents the number of stairs for the current nice staircase type
    # being considered. The smallest nice staircase has n_stairs = 1 (which is 2^1 - 1).
    n_stairs = 1

    while True:
        # Calculate the cost (total cells) for a staircase with `n_stairs`.
        # The formula is n * (n + 1) / 2.
        # Since `n_stairs` is always of the form 2^k - 1, then `n_stairs + 1` is 2^k.
        # So, the cost can also be written as (2^k - 1) * 2^k / 2, which simplifies
        # to (2^k - 1) * 2^(k-1).
        # Python's integer division (//) handles this correctly.
        current_staircase_cost = n_stairs * (n_stairs + 1) // 2

        # Check if we have enough cells to build this staircase.
        if total_cells_x >= current_staircase_cost:
            # If affordable, subtract its cost from the total available cells.
            total_cells_x -= current_staircase_cost
            # Increment the count of built staircases.
            count += 1
            # Move to the next larger nice staircase type.
            # If the current `n_stairs` is 2^k - 1, the next one in the sequence
            # is 2^(k+1) - 1. This can be calculated as 2 * (2^k - 1) + 1,
            # which simplifies to 2 * n_stairs + 1.
            n_stairs = 2 * n_stairs + 1
        else:
            # If the current staircase is too expensive, we cannot afford any
            # larger nice staircases either (as their costs are strictly increasing).
            # So, we break the loop.
            break

    return count
```