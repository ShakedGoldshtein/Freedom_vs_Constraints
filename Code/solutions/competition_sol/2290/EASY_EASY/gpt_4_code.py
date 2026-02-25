```python
def max_area(H, W, S):
    G = [[False] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            G[i][j] = S[i][j] == '#'
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    recth = [[0] * (W + 1) for _ in range(H + 1)]
    ans = max(H, W)
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if G[i][j] == G[i+1][j] and G[i][j] == G[i][j+1] and G[i][j] != G[i+1][j+1]:
                dp[i][j] = min(dp[i+1][j+1], dp[i][j+1], dp[i+1][j]) + 1
            else:
                dp[i][j] = 0
            recth[i][j] = max(recth[i+1][j], dp[i][j])
            ans = max(ans, (recth[i][j]+1) * (dp[i][j]+1))
    return ans
```