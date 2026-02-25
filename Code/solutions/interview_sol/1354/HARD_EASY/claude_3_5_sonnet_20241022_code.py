```python
def build_graph(n, edges):
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def dfs(node, parent, graph, dp, k):
    MOD = 10**9 + 7
    ways = [1] * (k+1)

    for neighbor in graph[node]:
        if neighbor != parent:
            child_ways = dfs(neighbor, node, graph, dp, k)
            
            # Ways where parent and child have same color
            for color in range(1, k+1):
                ways[color] = (ways[color] * child_ways[color]) % MOD
                
            # Ways where parent and child have different colors
            # Not needed for this problem per requirement

    return ways

def solve_testcase(n, k, edges):
    MOD = 10**9 + 7
    graph = build_graph(n, edges)
    
    # dp[i][j] = number of ways to color subtree rooted at i 
    # with root having color j
    dp = [[0]*(k+1) for _ in range(n+1)]
    
    # Get ways for each root color
    ways = dfs(1, 0, graph, dp, k)
    
    # Sum up ways for all possible root colors
    total = 0
    for color in range(1, k+1):
        total = (total + ways[color]) % MOD
        
    return total

def solve(T, cases):
    results = []
    for _ in range(T):
        n, k = cases[_][0]
        edges = cases[_][1:]
        result = solve_testcase(n, k, edges)
        results.append(result)
    return results
```