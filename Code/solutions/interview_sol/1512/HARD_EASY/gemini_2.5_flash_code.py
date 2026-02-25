```python
def solve_game(n: int, m: int) -> str:
    """
    Determines the winner of a game played on an N x M board, starting at (1,1).

    The game is an impartial game, which can be solved using the Sprague-Grundy theorem.
    It can be modeled as a sum of two independent games:
    1. A game played on the rows: moves are 1, 2, or 3 steps 'up' (increasing row index).
       The target row is N.
    2. A game played on the columns: moves are 1 or 2 steps 'right' (increasing column index).
       The target column is M.

    The Grundy value (or nim-value) of a game state (r, c) is g_row(r) XOR g_col(c).
    The player whose turn it is at a state with a non-zero Grundy value wins (Winning state).
    The player whose turn it is at a state with a zero Grundy value loses (Losing state).

    For the row game (moves 1, 2, or 3 cells up towards row N):
    The Grundy values for distances from N (N-r) follow a pattern:
    g_row(r) = (N - r) % 4
    For the starting row (1), the Grundy value is (N - 1) % 4.

    For the column game (moves 1 or 2 cells right towards column M):
    The Grundy values for distances from M (M-c) follow a pattern:
    g_col(c) = (M - c) % 3
    For the starting column (1), the Grundy value is (M - 1) % 3.

    The overall Grundy value for the starting position (1, 1) is g_row(1) XOR g_col(1).
    Tuzik (the first player) wins if this value is non-zero, otherwise Vanya (the second player) wins.

    Args:
        n: The total number of rows on the board (N).
        m: The total number of columns on the board (M).

    Returns:
        "Tuzik" if the first player wins, "Vanya" if the second player wins.
    """
    # Calculate the Grundy value for the row dimension.
    # The 'distance' from the starting row (1) to the target row (N) is N-1.
    # Moves are 1, 2, or 3 steps, leading to a cycle of 4 for Grundy values.
    grundy_row = (n - 1) % 4

    # Calculate the Grundy value for the column dimension.
    # The 'distance' from the starting column (1) to the target column (M) is M-1.
    # Moves are 1 or 2 steps, leading to a cycle of 3 for Grundy values.
    grundy_col = (m - 1) % 3

    # The Grundy value of the combined game is the XOR sum of the individual Grundy values.
    total_grundy_value = grundy_row ^ grundy_col

    # If the total Grundy value for the initial state is non-zero,
    # the first player (Tuzik) has a winning strategy.
    # Otherwise, the second player (Vanya) has a winning strategy.
    if total_grundy_value != 0:
        return "Tuzik"
    else:
        return "Vanya"
```