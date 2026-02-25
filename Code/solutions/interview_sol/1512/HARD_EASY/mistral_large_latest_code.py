```python
def determine_winner(test_cases):
    """
    Determines the winner of the game between Tuzik and Vanya for each test case.
    Both players play optimally, and the winner is determined based on the initial
    position (1, 1) and the board dimensions N x M.

    Args:
        test_cases: A list of tuples, where each tuple contains two integers (N, M)
                   representing the dimensions of the board for a test case.

    Returns:
        A list of strings ("Tuzik" or "Vanya") indicating the winner for each test case.
    """
    results = []
    for N, M in test_cases:
        # Calculate the difference from the target position (N, M) to (1, 1)
        delta_row = N - 1
        delta_col = M - 1

        # Determine the winner based on the modulo 4 of the differences
        if (delta_row % 4 == 0 and delta_col % 4 == 0) or \
           (delta_row % 4 == 1 and delta_col % 4 == 1) or \
           (delta_row % 4 == 2 and delta_col % 4 == 2) or \
           (delta_row % 4 == 3 and delta_col % 4 == 3):
            results.append("Vanya")
        else:
            results.append("Tuzik")
    return results
```