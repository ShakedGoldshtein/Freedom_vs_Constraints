```python
from collections import defaultdict
from functools import lru_cache
MOD = 10**9+7
MAX_N = 100000
BIN = (1, 2)

def add_edge(u, v):
    adj[u].append(v)
    adj[v].append(u)

def add_constraints(u, v, x):
    isX[u][v][0] = x
    isX[u][v][1] = x^1
    isX[v][u][0] = x
    isX[v][u][1] = x^1

@lru_cache(maxsize=None)
def dfs(v, par, i):
    dp[v][i][0] = dp[v][i][1] = 1
    for u in adj[v]:
        if u == par: continue
        dfs(u, v, i)
        dp[v][i][0] = (dp[v][i][0]*((dp[u][i][0]+dp[u][i][1])%MOD))%MOD
        dp[v][i][1] = (dp[v][i][1]*dp[u][i][isX[u][v][i]])%MOD
    if i: dp[v][i][0], dp[v][i][1] = dp[v][i][1], dp[v][i][0]

def solve(n, Q, edges, constraints):
    global adj, isX, dp
    adj = defaultdict(list)
    for u, v in edges: 
        add_edge(u, v)
    isX = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    for u, v, x in constraints: 
        add_constraints(u, v, x)
    dp = [[[0, 0] for _ in range(2)] for _ in range(n+1)]
    dfs(1, 0, 0)
    dfs(1, 0, 1)
    return (dp[1][0][0]+dp[1][0][1]*dp[1][1][1])%MOD

T = int(input())
for _ in range(T):
    n, Q = map(int, input().split())
    edges = [tuple(map(int,input().split())) for _ in range(n-1)]
    constraints = [tuple(map(int,input().split())) for _ in range(Q)]
    print(solve(n, Q, edges, constraints))
```