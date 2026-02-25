```python
def solve(n):
    if n < 0:
        return None
    if n == 0:
        return '0'
    if n == 1:
        return '01'
        
    dp = ['0', '01']
    
    for i in range(2, n + 1):
        dp.append(dp[i-1] + dp[i-2])
        
    return dp[n]
```