```python
def solve_game(n, rows):
    def get_best_score(dp, row, l, r, turn):
        if row >= n:
            return 0
        
        if l[row] > r[row]:
            return get_best_score(dp, row + 1, l, r, turn)
            
        state = (row, l[row], r[row], turn)
        if state in dp:
            return dp[state]
        
        if turn == 0: # Chef's turn
            # Take from current row
            score1 = coins[row][l[row]] + get_best_score(dp, row, l[row] + 1, r[row], 1)
            # Skip current row
            score2 = get_best_score(dp, row + 1, l, r, turn)
            dp[state] = max(score1, score2)
            
        else: # Ramsay's turn
            # Take from current row
            score1 = get_best_score(dp, row, l[row], r[row] - 1, 0)
            # Skip current row
            score2 = get_best_score(dp, row + 1, l, r, turn)
            dp[state] = min(score1, score2)
            
        return dp[state]

    # Create arrays to track remaining coins in each row
    coins = []
    left = []
    right = []
    
    for row in rows:
        coins.append(row[1:]) # Skip the count
        left.append(0)
        right.append(len(row) - 1)
    
    dp = {}
    return get_best_score(dp, 0, left, right, 0)

def solve(T, test_cases):
    results = []
    for _ in range(T):
        n = test_cases[_][0] 
        rows = test_cases[_][1:]
        results.append(solve_game(n, rows))
    return results
```