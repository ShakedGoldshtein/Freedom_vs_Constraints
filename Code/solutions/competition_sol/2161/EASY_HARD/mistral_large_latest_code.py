```python
def solve(n, m, w, weights, beauties, friendships):
    parent = [i for i in range(n + 1)]

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root != v_root:
            parent[v_root] = u_root

    for x, y in friendships:
        union(x, y)

    groups = {}
    for i in range(1, n + 1):
        root = find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)

    dp = [0] * (w + 1)
    for group in groups.values():
        total_weight = sum(weights[i-1] for i in group)
        total_beauty = sum(beauties[i-1] for i in group)
        max_beauty = 0
        best_single = 0
        for i in group:
            if weights[i-1] <= w:
                best_single = max(best_single, beauties[i-1])
        new_dp = dp.copy()
        for weight in range(w + 1):
            if weight >= total_weight:
                new_dp[weight] = max(new_dp[weight], dp[weight - total_weight] + total_beauty)
            for i in group:
                if weight >= weights[i-1]:
                    new_beauty = dp[weight - weights[i-1]] + beauties[i-1]
                    new_dp[weight] = max(new_dp[weight], new_beauty)
        dp = [max(dp[i], new_dp[i]) for i in range(w + 1)]
    return max(dp)
```