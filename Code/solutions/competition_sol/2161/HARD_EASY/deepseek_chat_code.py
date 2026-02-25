```python
def solve(n, m, w, weights, beauties, friendships):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for x, y in friendships:
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)
    
    visited = [False] * n
    groups = []
    
    for i in range(n):
        if not visited[i]:
            queue = deque([i])
            visited[i] = True
            group = []
            while queue:
                node = queue.popleft()
                group.append(node)
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            groups.append(group)
    
    dp = [0] * (w + 1)
    
    for group in groups:
        group_weight = 0
        group_beauty = 0
        group_items = []
        
        for idx in group:
            group_weight += weights[idx]
            group_beauty += beauties[idx]
            group_items.append((weights[idx], beauties[idx]))
        
        new_dp = dp[:]
        
        for cap in range(w, -1, -1):
            if cap + group_weight <= w:
                new_dp[cap + group_weight] = max(new_dp[cap + group_weight], dp[cap] + group_beauty)
        
        for weight, beauty in group_items:
            for cap in range(w - weight, -1, -1):
                new_dp[cap + weight] = max(new_dp[cap + weight], dp[cap] + beauty)
        
        dp = new_dp
    
    return max(dp)
```