```python
MOD = 10**9 + 7

def solve(s):
    if 'c' in s or 'k' in s:
        return 0
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if i >= 2 and s[i-2:i] == "ff":
            dp[i] = (dp[i] + dp[i - 2]) % MOD
        elif i >= 2 and s[i-2:i] == "gg":
            dp[i] = (dp[i] + dp[i - 2]) % MOD
    
    return dp[n]
```