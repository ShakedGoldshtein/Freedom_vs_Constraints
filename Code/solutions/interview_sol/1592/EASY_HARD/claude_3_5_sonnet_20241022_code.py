```python
def solve(N, rows):
    def get_optimal(left, right, dp, turn):
        if left[0] > right[0] or left[1] > right[1]:
            return 0
            
        state = (left[0], left[1], right[0], right[1], turn)
        if state in dp:
            return dp[state]
            
        if turn == 0: # Chef's turn
            best = float('-inf')
            # Try taking from each row
            for row in range(N):
                if left[row] <= right[row]:
                    val = coins[row][left[row]]
                    new_left = list(left)
                    new_left[row] += 1
                    score = val + get_optimal(tuple(new_left), right, dp, 1)
                    best = max(best, score)
            dp[state] = best
            return best
            
        else: # Ramsay's turn 
            best = float('inf')
            for row in range(N):
                if left[row] <= right[row]:
                    new_right = list(right)
                    new_right[row] -= 1
                    score = get_optimal(left, tuple(new_right), dp, 0)
                    best = min(best, score)
            dp[state] = best
            return best
            
    coins = []
    for row in rows:
        coins.append(row[1:])
        
    left = tuple([0] * N) # leftmost index for each row
    right = tuple([len(coins[i])-1 for i in range(N)]) # rightmost index
    dp = {}
    
    result = get_optimal(left, right, dp, 0)
    return result

```