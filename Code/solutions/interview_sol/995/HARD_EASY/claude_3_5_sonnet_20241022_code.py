```python
def max_money_from_rooms(n: int, money: list[int], k: int) -> int:
    """
    Calculate maximum money obtainable from n rooms using k keys.
    
    Args:
        n: Number of rooms
        money: List of money amounts in each room
        k: Number of keys available
        
    Returns:
        Maximum money obtainable
    """
    # Edge cases
    if n == 0 or k == 0:
        return 0
    if k >= n:
        return sum(money)
    
    # dp[i][j][side] represents max money with i keys used,
    # having reached index j from left (side=0) or right (side=1)
    dp = [[[0]*2 for _ in range(n)] for _ in range(k+1)]
    
    # Initialize base cases - can only start from corners
    dp[1][0][0] = money[0]  # Left corner
    dp[1][n-1][1] = money[n-1]  # Right corner
    
    # For each number of keys used
    for keys in range(1, k+1):
        # For each position
        for pos in range(n):
            # Coming from left side
            if dp[keys][pos][0] > 0:
                # Can move right if room available
                if pos + 1 < n:
                    dp[keys+1][pos+1][0] = max(
                        dp[keys+1][pos+1][0],
                        dp[keys][pos][0] + money[pos+1]
                    )
                # Can move left if room available
                if pos - 1 >= 0:
                    dp[keys+1][pos-1][0] = max(
                        dp[keys+1][pos-1][0],
                        dp[keys][pos][0] + money[pos-1]
                    )
                    
            # Coming from right side
            if dp[keys][pos][1] > 0:
                # Can move right if room available
                if pos + 1 < n:
                    dp[keys+1][pos+1][1] = max(
                        dp[keys+1][pos+1][1],
                        dp[keys][pos][1] + money[pos+1]
                    )
                # Can move left if room available  
                if pos - 1 >= 0:
                    dp[keys+1][pos-1][1] = max(
                        dp[keys+1][pos-1][1],
                        dp[keys][pos][1] + money[pos-1]
                    )
    
    # Find maximum money across all positions and both sides
    max_money = 0
    for pos in range(n):
        max_money = max(max_money, dp[k][pos][0], dp[k][pos][1])
        
    return max_money
```