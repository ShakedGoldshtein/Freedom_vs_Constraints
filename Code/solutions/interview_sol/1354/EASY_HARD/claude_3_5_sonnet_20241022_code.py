```python
def build_graph(n, edges):
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def dfs(graph, visited, node, n, k, dp):
    visited[node] = True
    curr_count = k
    node_visited = []
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            node_visited.append(neighbor)
            dfs(graph, visited, neighbor, n, k, dp)
            
    if not node_visited:
        dp[node] = k
        return
        
    first = node_visited[0]
    dp[node] = (k * dp[first]) % 1000000007
    
    for i in range(1, len(node_visited)):
        curr = node_visited[i]
        dp[node] *= dp[curr]
        dp[node] //= k
        dp[node] %= 1000000007

def solve(n, k, edges):
    MOD = 1000000007
    
    if n == 1:
        return k % MOD
        
    graph = build_graph(n, edges)
    visited = [False] * (n+1)
    dp = [0] * (n+1)
    
    dfs(graph, visited, 1, n, k, dp)
    
    return dp[1]

def solve_multiple_testcases(testcases):
    result = []
    for n, k, edges in testcases:
        result.append(solve(n, k, edges))
    return result
```