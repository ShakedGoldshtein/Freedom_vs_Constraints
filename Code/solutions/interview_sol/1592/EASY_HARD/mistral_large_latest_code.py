```python
def solve(test_cases):
    results = []
    for case in test_cases:
        N, rows = case
        total = 0
        for row in rows:
            C, coins = row
            if C == 0:
                continue
            prefix = [0] * (C + 1)
            suffix = [0] * (C + 1)
            for i in range(1, C + 1):
                prefix[i] = prefix[i - 1] + coins[i - 1]
            for i in range(C - 1, -1, -1):
                suffix[i] = suffix[i + 1] + coins[i]
            dp = [[-1 for _ in range(C + 1)] for __ in range(C + 1)]
            def dfs(l, r, turn):
                if l > r:
                    return 0
                if dp[l][r] != -1:
                    return dp[l][r]
                if turn == 0:
                    res = max(dfs(l + 1, r, 1) + coins[l], dfs(l, r - 1, 1))
                else:
                    if (r - l) % 2 == 0:
                        res = max(dfs(l + 1, r, 0), dfs(l, r - 1, 0))
                    else:
                        res = min(dfs(l + 1, r, 0), dfs(l, r - 1, 0))
                dp[l][r] = res
                return res
            total += dfs(0, C - 1, 0)
        results.append(total)
    return results
```