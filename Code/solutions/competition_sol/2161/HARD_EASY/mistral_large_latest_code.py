```python
def solve(n, m, w, weights, beauties, friendships):
    from collections import defaultdict, deque

    def build_friendship_groups(n, friendships):
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
        return groups

    groups = build_friendship_groups(n, friendships)

    dp = [0] * (w + 1)

    for group in groups:
        group_size = len(group)
        if group_size == 1:
            hos = group[0]
            current_weight = weights[hos]
            current_beauty = beauties[hos]
            for remaining_weight in range(w, current_weight - 1, -1):
                if dp[remaining_weight - current_weight] + current_beauty > dp[remaining_weight]:
                    dp[remaining_weight] = dp[remaining_weight - current_weight] + current_beauty
        else:
            total_weight = sum(weights[hos] for hos in group)
            total_beauty = sum(beauties[hos] for hos in group)
            if total_weight <= w:
                for remaining_weight in range(w, total_weight - 1, -1):
                    if dp[remaining_weight - total_weight] + total_beauty > dp[remaining_weight]:
                        dp[remaining_weight] = dp[remaining_weight - total_weight] + total_beauty

            for hos in group:
                current_weight = weights[hos]
                current_beauty = beauties[hos]
                for remaining_weight in range(w, current_weight - 1, -1):
                    if dp[remaining_weight - current_weight] + current_beauty > dp[remaining_weight]:
                        dp[remaining_weight] = dp[remaining_weight - current_weight] + current_beauty

    return max(dp)
```