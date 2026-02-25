Here is the code based on above requirements:

```python
MOD = 10 ** 9 + 7

def numOfOddSumSubArrays(arr):
    n = len(arr)
    dp = [[0, 0] for _ in range(n + 1)]
    res = 0

    for i in range(1, n + 1):
        if arr[i - 1] % 2 == 0:
            dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = dp[i - 1][1]
        else:
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = dp[i - 1][0] + 1

        res += dp[i][1]

    return res % MOD
```
This function works by using dynamic programming. It maintains a 2D array of size n+1x2 called "dp", where dp[i][j] stores the number of sub-arrays ending at index i with sum as even (when j=0) or odd (when j=1). After looping through the array and calculating these numbers, it simply returns the sum of the number of all sub-arrays with odd sum, i.e., dp[i][1] for all i, modulo 10^9 + 7 to keep the number manageable.