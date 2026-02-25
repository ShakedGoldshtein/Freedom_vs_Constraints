```python
def min_fatigue(N: int, A: int, B: int, X: list) -> int:
    """
    Calculate minimum fatigue to visit all towns using walking and teleportation
    
    Args:
        N: Number of towns
        A: Fatigue per unit distance when walking
        B: Fatigue when teleporting
        X: List of town coordinates (1-indexed)
    
    Returns:
        Minimum total fatigue
    """
    # dp[i][j] represents min fatigue to reach town i, 
    # where j=0 means walked to i, j=1 means teleported to i
    dp = [[float('inf')] * 2 for _ in range(N)]
    
    # Base case: At starting town 1
    dp[0][0] = 0  # No fatigue at start
    dp[0][1] = 0  # No need to teleport to start
    
    # For each town after first
    for i in range(1, N):
        # Option 1: Walk from previous position
        # Can only walk if previous position was also walked to
        dp[i][0] = dp[i-1][0] + A * (X[i] - X[i-1])
        
        # Option 2: Teleport to current position
        # Find minimum of:
        # a) Teleporting after walking to any previous town
        # b) Teleporting after teleporting to any previous town
        min_prev = float('inf')
        for j in range(i):
            min_prev = min(min_prev, dp[j][0], dp[j][1])
        dp[i][1] = min_prev + B
    
    # Return minimum of walking or teleporting to final town
    return min(dp[N-1][0], dp[N-1][1])
```