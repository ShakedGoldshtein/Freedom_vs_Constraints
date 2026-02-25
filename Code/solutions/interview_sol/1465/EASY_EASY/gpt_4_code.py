```python
from collections import defaultdict
from sys import stdin, stdout
mod = 10**9+7

def addedge(u, v):
    a[u].append(v)
    a[v].append(u)

def dfs(u, p):
    dp[u][0][0] = dp[u][1][1] = 1
    for v in a[u]:
        if v == p:
            continue
        dfs(v, u)
        dp1 = [[0,0] for _ in range(2)]
        for cu in range(2):
            for cv in range(2):
                dp1[cu][0] += (dp[u][cu][0]*dp[v][cv][0] + dp[u][cu][1]*dp[v][cv][1])%mod
                dp1[cu][1] += (dp[u][cu][0]*dp[v][cv][1] + dp[u][cu][1]*dp[v][cv][0])%mod
        dp[u] = dp1
        
def solve(T, data):
    global dp
    global a
    result = []
    idx = 0
    while T>0:
        n = data[idx]
        idx += 1
        q = data[idx]
        idx += 1
        dp = [[[0, 0] for _ in range(2)] for _ in range(n+5)]
        a = defaultdict(list)
        for _ in range(n-1):
            u = data[idx]
            idx += 1
            v = data[idx]
            idx += 1
            addedge(u, v)
        dfs(1, 0)
        ans1, ans0 = 1, 1
        for _ in range(q):
            u = data[idx]
            idx += 1
            v = data[idx]
            idx += 1
            x = data[idx]
            idx += 1
            if (level[u]+level[v])%2 == x:
                ans1 = (ans1*dp[1][0][0])%mod
                ans0 = (ans0*dp[1][0][0])%mod
            else:
                ans1 = (ans1*dp[1][0][1])%mod
                ans0 = (ans0*dp[1][0][1])%mod
        result.append(ans1+ans0)
        T -= 1
    return result
```