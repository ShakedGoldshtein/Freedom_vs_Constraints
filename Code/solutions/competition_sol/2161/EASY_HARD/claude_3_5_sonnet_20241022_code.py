```python
def solve(n, m, w, weights, beauties, friends):
    # Build adjacency list for friend groups
    adj = [[] for _ in range(n)]
    for x, y in friends:
        adj[x-1].append(y-1)
        adj[y-1].append(x-1)
        
    # Find friend groups using DFS
    groups = []
    visited = [False] * n
    
    def dfs(v, group):
        visited[v] = True
        group.append(v)
        for u in adj[v]:
            if not visited[u]:
                dfs(u, group)
    
    for v in range(n):
        if not visited[v]:
            group = []
            dfs(v, group)
            groups.append(group)
            
    # For each group, either take all members or take the best single member
    dp = [[0] * (w+1) for _ in range(len(groups)+1)]
    
    for i in range(1, len(groups)+1):
        group = groups[i-1]
        
        # Calculate total weight and beauty for whole group
        group_weight = sum(weights[j] for j in group)
        group_beauty = sum(beauties[j] for j in group)
        
        # Find best single member in group
        best_single_weight = float('inf')
        best_single_beauty = 0
        for j in group:
            if weights[j] < best_single_weight:
                best_single_weight = weights[j]
                best_single_beauty = beauties[j]
            elif weights[j] == best_single_weight:
                best_single_beauty = max(best_single_beauty, beauties[j])
        
        for j in range(w+1):
            # Don't take any from this group
            dp[i][j] = dp[i-1][j]
            
            # Take best single member if possible
            if j >= best_single_weight:
                dp[i][j] = max(dp[i][j], dp[i-1][j-best_single_weight] + best_single_beauty)
                
            # Take whole group if possible
            if j >= group_weight:
                dp[i][j] = max(dp[i][j], dp[i-1][j-group_weight] + group_beauty)
                
    return dp[len(groups)][w]
```