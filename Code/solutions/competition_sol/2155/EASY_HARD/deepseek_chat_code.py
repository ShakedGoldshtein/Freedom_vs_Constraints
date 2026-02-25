```python
def solve(n, m, grid):
    dp1 = [[0] * (m + 2) for _ in range(n + 2)]
    dp2 = [[0] * (m + 2) for _ in range(n + 2)]
    dp3 = [[0] * (m + 2) for _ in range(n + 2)]
    dp4 = [[0] * (m + 2) for _ in range(n + 2)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp1[i][j] = max(dp1[i-1][j], dp1[i][j-1]) + grid[i-1][j-1]
    
    for i in range(n, 0, -1):
        for j in range(1, m + 1):
            dp2[i][j] = max(dp2[i+1][j], dp2[i][j-1]) + grid[i-1][j-1]
    
    for i in range(1, n + 1):
        for j in range(m, 0, -1):
            dp3[i][j] = max(dp3[i-1][j], dp3[i][j+1]) + grid[i-1][j-1]
    
    for i in range(n, 0, -1):
        for j in range(m, 0, -1):
            dp4[i][j] = max(dp4[i+1][j], dp4[i][j+1]) + grid[i-1][j-1]
    
    ans = 0
    for i in range(2, n):
        for j in range(2, m):
            option1 = dp1[i-1][j] + dp4[i+1][j] + dp2[i][j-1] + dp3[i][j+1]
            option2 = dp1[i][j-1] + dp4[i][j+1] + dp2[i+1][j] + dp3[i-1][j]
            ans = max(ans, option1, option2)
    
    return ans
```