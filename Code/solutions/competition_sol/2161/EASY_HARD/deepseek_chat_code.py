```python
def solve(n, m, w, weights, beauties, friendships):
    parent = list(range(n))
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[ry] = rx
    
    for x, y in friendships:
        union(x-1, y-1)
    
    groups = {}
    for i in range(n):
        root = find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)
    
    dp = [0] * (w + 1)
    
    for group in groups.values():
        total_w = 0
        total_b = 0
        group_items = []
        for idx in group:
            total_w += weights[idx]
            total_b += beauties[idx]
            group_items.append((weights[idx], beauties[idx]))
        
        new_dp = dp[:]
        for cap in range(w, -1, -1):
            for wt, bt in group_items:
                if cap + wt <= w:
                    new_dp[cap + wt] = max(new_dp[cap + wt], dp[cap] + bt)
            if cap + total_w <= w:
                new_dp[cap + total_w] = max(new_dp[cap + total_w], dp[cap] + total_b)
        dp = new_dp
    
    return max(dp)
```