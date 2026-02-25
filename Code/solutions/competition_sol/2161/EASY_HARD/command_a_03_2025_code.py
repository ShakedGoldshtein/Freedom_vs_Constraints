```python
def solve(n: int, m: int, w: int, weights: list[int], beauties: list[int], friends: list[tuple[int, int]]) -> int:
    # Step 1: Build the friendship groups using Union-Find
    parent = list(range(n + 1))
    rank = [1] * (n + 1)

    def find(u: int) -> int:
        while parent[u] != u:
            parent[u] = parent[parent[u]]  # Path compression
            u = parent[u]
        return u

    def union(u: int, v: int) -> None:
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return
        if rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        else:
            parent[v_root] = u_root
            if rank[u_root] == rank[v_root]:
                rank[u_root] += 1

    for x, y in friends:
        union(x, y)

    # Step 2: Group Hoses by their friendship groups
    groups = {}
    for i in range(1, n + 1):
        root = find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)

    # Step 3: Calculate the total weight and beauty for each group
    group_info = []
    for root, members in groups.items():
        total_weight = sum(weights[i - 1] for i in members)
        total_beauty = sum(beauties[i - 1] for i in members)
        max_beauty = max(beauties[i - 1] for i in members)
        group_info.append((total_weight, total_beauty, max_beauty))

    # Step 4: Dynamic programming to find the maximum beauty
    dp = [0] * (w + 1)
    for total_weight, total_beauty, max_beauty in group_info:
        if total_weight <= w:
            for j in range(w, total_weight - 1, -1):
                dp[j] = max(dp[j], dp[j - total_weight] + total_beauty)
        for j in range(w, max_beauty - 1, -1):
            dp[j] = max(dp[j], dp[j - max_beauty] + max_beauty)

    return dp[w]
```