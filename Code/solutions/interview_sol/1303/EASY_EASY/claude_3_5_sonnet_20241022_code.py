```python
def solve(n, k, m, arr):
    MOD = 1000000007
    
    # dp[pos][len] stores count of valid subsequences ending at pos of length len
    dp = [[0]*(k+1) for _ in range(n)]
    
    # initialize dp for first elements
    for i in range(n):
        if arr[i] % m == 1 % m:
            dp[i][1] = 1
            
    # fill dp table
    for j in range(2, k+1):
        for i in range(j-1, n):
            if arr[i] % m == j % m:
                # add count of valid subsequences ending before i with length j-1
                for prev in range(j-2, i):
                    dp[i][j] = (dp[i][j] + dp[prev][j-1]) % MOD
                    
    # sum up all valid subsequences of length k
    ans = 0
    for i in range(k-1, n):
        ans = (ans + dp[i][k]) % MOD
        
    return ans

def solve_test_cases(t, test_cases):
    results = []
    for _ in range(t):
        n, k, m = test_cases[_][0]
        arr = test_cases[_][1]
        results.append(solve(n, k, m, arr))
    return results
```