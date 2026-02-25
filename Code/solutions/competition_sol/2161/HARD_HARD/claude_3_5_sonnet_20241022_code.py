```python
def find_groups(n, edges):
    groups = []
    visited = set()
    
    def dfs(node, curr_group):
        visited.add(node)
        curr_group.append(node)
        for edge in edges:
            if edge[0] == node and edge[1] not in visited:
                dfs(edge[1], curr_group)
            elif edge[1] == node and edge[0] not in visited:
                dfs(edge[0], curr_group)
    
    for i in range(n):
        if i not in visited:
            curr_group = []
            dfs(i, curr_group)
            groups.append(curr_group)
            
    return groups

def solve(n, m, w, weights, beauties, edges):
    # Find friendship groups using DFS
    groups = find_groups(n, edges)
    
    # For each group, compute total weight/beauty and single person max beauty
    group_data = []
    for group in groups:
        total_weight = sum(weights[i] for i in group)
        total_beauty = sum(beauties[i] for i in group)
        max_single = max((beauties[i], weights[i]) for i in group)
        group_data.append((total_weight, total_beauty, max_single))
    
    # DP array: dp[i][j] = max beauty with first i groups and j max weight
    dp = [[0] * (w + 1) for _ in range(len(groups) + 1)]
    
    # For each group
    for i in range(len(groups)):
        # For each possible weight limit
        for curr_w in range(w + 1):
            # Don't use this group
            dp[i + 1][curr_w] = dp[i][curr_w]
            
            # Use entire group if possible
            if curr_w >= group_data[i][0]:
                dp[i + 1][curr_w] = max(
                    dp[i + 1][curr_w],
                    dp[i][curr_w - group_data[i][0]] + group_data[i][1]
                )
            
            # Use single person if possible    
            if curr_w >= group_data[i][2][1]:
                dp[i + 1][curr_w] = max(
                    dp[i + 1][curr_w], 
                    dp[i][curr_w - group_data[i][2][1]] + group_data[i][2][0]
                )
    
    return dp[len(groups)][w]
```