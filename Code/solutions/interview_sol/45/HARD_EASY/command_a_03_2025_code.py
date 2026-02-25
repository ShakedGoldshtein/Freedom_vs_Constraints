```python
def count_nice_staircases(x: int) -> int:
    """
    Counts the maximal number of different nice staircases that can be built using no more than x cells.

    A nice staircase is one that can be covered by n disjoint squares, where n is the number of stairs.
    The function calculates the number of such staircases by iterating through possible values of n
    and checking if the total cells used do not exceed x.

    Args:
        x (int): The total number of cells available for building staircases.

    Returns:
        int: The maximal number of different nice staircases that can be built.
    """
    count = 0
    n = 1
    while True:
        # Calculate the total cells required for n stairs
        # The sum of squares of the first n natural numbers is n*(n+1)*(2n+1)/6
        total_cells = n * (n + 1) * (2 * n + 1) // 6
        if total_cells > x:
            break
        count += 1
        n += 1
    return count


def solve(t: int, test_cases: list[int]) -> list[int]:
    """
    Solves the problem for multiple test cases.

    Args:
        t (int): The number of test cases.
        test_cases (list[int]): A list of integers representing the number of cells for each test case.

    Returns:
        list[int]: A list of integers representing the number of nice staircases for each test case.
    """
    results = []
    for x in test_cases:
        results.append(count_nice_staircases(x))
    return results
```