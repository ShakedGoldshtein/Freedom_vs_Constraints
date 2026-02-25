```python
def maxSumDivThree(nums):
    dp = [0, 0, 0]
    for num in nums:
        for i in dp[:]:
            dp[(i + num) % 3] = max(dp[(i + num) % 3], i + num)
    return dp[0]
```