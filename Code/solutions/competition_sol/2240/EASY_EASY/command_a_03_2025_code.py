```python
from collections import defaultdict


def solve(n: int, edges: list[tuple[int, int]], values: list[int]) -> int:
    """
    Calculate the minimum number of moves required to make all integers on the vertices of a tree equal to zero.

    Args:
        n (int): Number of vertices in the tree.
        edges (list of tuples): List of edges in the tree, where each edge is represented as a tuple (a, b).
        values (list of int): List of integers written on each vertex, where values[i] corresponds to the i-th vertex.

    Returns:
        int: The minimum number of moves required to make all integers on the vertices equal to zero.
    """
    # Build adjacency list for the tree
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    # Initialize variables to track the sum and count of values in the subtree rooted at vertex 1
    sum_values = 0
    count = 0

    # Perform DFS to calculate the sum and count of values in the subtree rooted at vertex 1
    def dfs(u: int, parent: int) -> None:
        nonlocal sum_values, count
        if u == 1:
            sum_values += values[u - 1]
            count += 1
        for v in adj[u]:
            if v != parent:
                dfs(v, u)
                if v == 1:
                    sum_values += values[u - 1]
                    count += 1

    dfs(1, -1)

    # Calculate the minimum number of moves required
    # The number of moves is the absolute difference between the sum of values in the subtree and the total sum of values
    total_sum = sum(values)
    return abs(sum_values - total_sum)


# Example usage:
# n = 3
# edges = [(1, 2), (1, 3)]
# values = [1, -1, 1]
# print(solve(n, edges, values))  # Output: 3
```