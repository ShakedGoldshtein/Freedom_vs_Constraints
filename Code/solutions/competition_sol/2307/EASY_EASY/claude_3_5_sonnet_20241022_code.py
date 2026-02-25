```python
def solve(n, a, b, x):
    dp = [float('inf')] * n
    dp[0] = 0
    
    for i in range(1, n):
        # Try reaching town i from each previous town j
        for j in range(i):
            # Option 1: Walk from j to i
            walk_cost = (x[i] - x[j]) * a
            dp[i] = min(dp[i], dp[j] + walk_cost)
            
            # Option 2: Teleport from j to i
            dp[i] = min(dp[i], dp[j] + b)
    
    return dp[n-1]
```