```python
from collections import defaultdict, deque


def find_friendship_groups(n: int, friends: list[tuple[int, int]]) -> list[list[int]]:
    """
    Finds all friendship groups in the graph.

    Args:
        n (int): Number of Hoses.
        friends (list of tuples): List of friend pairs.

    Returns:
        list of lists: Each sublist represents a friendship group.
    """
    graph = defaultdict(list)
    for u, v in friends:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    visited = [False] * n
    groups = []
    for i in range(n):
        if not visited[i]:
            group = []
            queue = deque([i])
            visited[i] = True
            while queue:
                node = queue.popleft()
                group.append(node)
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            groups.append(group)
    return groups


def solve(
    n: int, m: int, w: int, weights: list[int], beauties: list[int], friends: list[tuple[int, int]]
) -> int:
    """
    Solves the problem of maximizing the total beauty of invited Hoses without exceeding the weight limit.

    Args:
        n (int): Number of Hoses.
        m (int): Number of friend pairs.
        w (int): Maximum total weight allowed.
        weights (list of int): Weights of the Hoses.
        beauties (list of int): Beauties of the Hoses.
        friends (list of tuples): List of friend pairs.

    Returns:
        int: Maximum possible total beauty.
    """
    groups = find_friendship_groups(n, friends)
    max_beauty = 0

    # Iterate over all possible combinations of selecting either all or one from each group
    for mask in range(0, 2 ** len(groups)):
        total_weight = 0
        total_beauty = 0
        valid = True

        for i, group in enumerate(groups):
            if mask & (1 << i):
                # Select all Hoses in the group
                group_weight = sum(weights[j] for j in group)
                group_beauty = sum(beauties[j] for j in group)
                if group_weight > w:
                    valid = False
                    break
                total_weight += group_weight
                total_beauty += group_beauty
            else:
                # Select at most one Hos from the group
                best_beauty = -1
                best_weight = float("inf")
                for j in group:
                    if weights[j] < best_weight:
                        best_beauty = beauties[j]
                        best_weight = weights[j]
                if best_beauty != -1:
                    total_weight += best_weight
                    total_beauty += best_beauty

        if valid and total_weight <= w and total_beauty > max_beauty:
            max_beauty = total_beauty

    return max_beauty
```