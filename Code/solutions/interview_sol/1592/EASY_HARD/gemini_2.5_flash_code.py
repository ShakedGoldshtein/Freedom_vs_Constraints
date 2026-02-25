```python
def get_max_chef_money(N, rows):
    """
    Calculates the maximum amount of money Chef can earn in the game.

    Args:
        N (int): The number of rows of coins.
        rows (list of list of int): A list where each element is a list of coin
                                     values for a specific row.
                                     Example: [[5, 2, 3, 4], [1, 6]]

    Returns:
        int: The maximum amount of money Chef can earn.
    """
    total_chef_score = 0

    # The key insight for this problem, given the specific rules (Chef takes leftmost,
    # Ramsay takes rightmost) and optimal play from both sides, is that the choices
    # made by Chef within a row do not conflict with Ramsay's choices within the same row.
    # Chef will always only have access to the leftmost available coin, and Ramsay to the
    # rightmost available coin. Their "paths" of taking coins from a row converge
    # from opposite ends.
    #
    # Therefore, the set of coins Chef takes from a specific row `i` is independent
    # of when he chooses that row or when Ramsay chooses that row. He will always take
    # the first `ceil(C_i / 2)` coins from the left end of row `i` (i.e., A_i,1, A_i,2, ...).
    # Similarly, Ramsay will always take the first `floor(C_i / 2)` coins from the
    # right end of row `i` (i.e., A_i,C_i, A_i,C_i-1, ...).
    #
    # Chef's total score is simply the sum of the scores he would get from each
    # row if that row were played in isolation according to his rules.

    for coins_in_row in rows:
        C_i = len(coins_in_row)

        # Calculate how many coins Chef would take from this row if played in isolation.
        # Since Chef plays first and they alternate on this row, Chef takes coins
        # on turns 0, 2, 4, ...
        # This means Chef takes ceil(C_i / 2) coins.
        chef_moves_on_this_row = (C_i + 1) // 2 
        
        current_row_chef_score = 0
        for k in range(chef_moves_on_this_row):
            current_row_chef_score += coins_in_row[k]
        
        total_chef_score += current_row_chef_score
        
    return total_chef_score
```