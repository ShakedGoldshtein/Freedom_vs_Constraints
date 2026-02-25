```python
def num_of_ways(T, tests):
    dp = [[0]*1001 for _ in range(1001)]
    dp[1][0] = 1
    dp[1][1] = 2
    dp[0][1] = 1
    dp[2][1] = 3 

    for V in range(max(2, tests[0][0], tests[0][1])+1, 1001):
        dp[V][0] = 1
        dp[V][1] = V + 1
        dp[0][V] = 1
        for W in range(2, V+1):
            dp[V][W] = (dp[V-1][W-2] + dp[V-1][W-1] + dp[V-1][W]) % 1000000007
        for W in range(V+1, 1001):
            dp[V][W] = (dp[V-1][W-1] + dp[V-1][W]) % 1000000007

    ans = []
    for i in range(T):
        V, W = tests[i]
        ans.append(dp[V][W % 1000000007])
    return ans 
```
