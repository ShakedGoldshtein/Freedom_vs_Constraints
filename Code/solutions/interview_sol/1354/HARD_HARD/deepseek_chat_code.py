```python
MOD = 10**9 + 7

def solve_test_case(n, k, edges):
    if n == 0:
        return 0
    
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    if k == 0:
        return 0
    
    dp = [[0] * (k + 1) for _ in range(n)]
    
    def dfs(u, parent):
        for v in graph[u]:
            if v != parent:
                dfs(v, u)
        
        for color in range(1, k + 1):
            ways = 1
            for v in graph[u]:
                if v == parent:
                    continue
                total = 0
                for c in range(1, k + 1):
                    if c != color:
                        total = (total + dp[v][c]) % MOD
                ways = (ways * total) % MOD
            dp[u][color] = ways
    
    dfs(0, -1)
    
    total_ways = 0
    for color in range(1, k + 1):
        total_ways = (total_ways + dp[0][color]) % MOD
    
    return total_ways

def main(T, test_cases):
    results = []
    for i in range(T):
        n, k = test_cases[i][0]
        edges = test_cases[i][1]
        results.append(solve_test_case(n, k, edges))
    return results
```