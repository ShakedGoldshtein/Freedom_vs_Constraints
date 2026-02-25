```python
MOD = 10**9 + 7

def solve(T, test_cases):
    results = []
    for case in test_cases:
        n, k = case[0]
        edges = case[1]
        
        if n == 0:
            results.append(0)
            continue
            
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        if k == 1:
            results.append(1)
            continue
            
        dp = [[0] * (k+1) for _ in range(n)]
        
        def dfs(u, parent):
            for v in adj[u]:
                if v == parent:
                    continue
                dfs(v, u)
            
            for color in range(1, k+1):
                ways = 1
                for v in adj[u]:
                    if v == parent:
                        continue
                    total = 0
                    for c in range(1, k+1):
                        if c != color:
                            total = (total + dp[v][c]) % MOD
                    ways = (ways * total) % MOD
                dp[u][color] = ways
        
        dfs(0, -1)
        total_ways = 0
        for color in range(1, k+1):
            total_ways = (total_ways + dp[0][color]) % MOD
        results.append(total_ways)
    
    return results
```