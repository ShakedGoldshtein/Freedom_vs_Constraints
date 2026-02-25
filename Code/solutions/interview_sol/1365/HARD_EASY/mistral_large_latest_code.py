```python
MOD = 10**9 + 7

def count_unique_strings(s: str) -> int:
    if not s:
        return 0

    # Check if the string contains 'c' or 'k'
    if 'c' in s or 'k' in s:
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty string has one way

    for i in range(1, n + 1):
        dp[i] = dp[i - 1]  # Default: carry forward previous count

        # Check for 'ff' (from 'c')
        if i >= 2 and s[i - 2:i] == 'ff':
            dp[i] = (dp[i] + dp[i - 2]) % MOD

        # Check for 'gg' (from 'k')
        if i >= 2 and s[i - 2:i] == 'gg':
            dp[i] = (dp[i] + dp[i - 2]) % MOD

    return dp[n]
```