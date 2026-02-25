```python
def solve(s):
    MOD = 1000000007
    
    # Check if input string contains c or k
    if 'c' in s or 'k' in s:
        return 0
        
    # dp[i][0] = number of ways for s[0:i] without ff/gg at position i-1
    # dp[i][1] = number of ways for s[0:i] with ff at position i-1 
    # dp[i][2] = number of ways for s[0:i] with gg at position i-1
    dp = [[0,0,0] for _ in range(len(s)+1)]
    dp[0][0] = 1
    
    for i in range(len(s)):
        if s[i] == 'f':
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = (dp[i][0] + dp[i][1]) % MOD
            dp[i+1][2] = dp[i][2]
        elif s[i] == 'g':
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][1]
            dp[i+1][2] = (dp[i][0] + dp[i][2]) % MOD
        else:
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][1] 
            dp[i+1][2] = dp[i][2]
            
    return sum(dp[-1]) % MOD
```