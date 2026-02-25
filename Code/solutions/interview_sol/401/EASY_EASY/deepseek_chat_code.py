```python
def maxSumDivThree(nums):
    dp = [0, -10**9, -10**9]
    for num in nums:
        mod = num % 3
        new_dp = dp[:]
        for i in range(3):
            new_dp[(i + mod) % 3] = max(new_dp[(i + mod) % 3], dp[i] + num)
        dp = new_dp
    return dp[0]
```