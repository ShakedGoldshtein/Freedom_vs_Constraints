```python
def solve(t: int, test_cases: list[int]) -> list[int]:
    """
    Solves the problem of finding the maximal number of different nice staircases
    that can be built using no more than x cells in total.

    Args:
        t (int): The number of test cases.
        test_cases (list[int]): A list of integers representing the number of cells for each test case.

    Returns:
        list[int]: A list of integers representing the number of different nice staircases for each test case.
    """
    results = []
    for x in test_cases:
        # Initialize the count of nice staircases
        count = 0
        # Initialize the current number of cells used
        total_cells = 0
        # Initialize the current number of stairs
        stairs = 1
        # Loop until the total cells exceed x
        while True:
            # Calculate the cells needed for the current staircase
            cells_needed = stairs * (stairs + 1) // 2
            # If adding the current staircase exceeds x, break
            if total_cells + cells_needed > x:
                break
            # Add the current staircase to the total cells
            total_cells += cells_needed
            # Increment the count of nice staircases
            count += 1
            # Move to the next staircase
            stairs += 1
        results.append(count)
    return results


# Read input
t = int(input())
test_cases = [int(input()) for _ in range(t)]

# Compute results
results = solve(t, test_cases)

# Output results
for result in results:
    print(result)
```