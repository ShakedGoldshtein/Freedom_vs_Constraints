```python
MOD = 10**9 + 7

def solve(n: int, k: int, edges: list[tuple[int, int]]) -> int:
    from collections import defaultdict
    from functools import lru_cache

    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Find the diameter of the tree
    def bfs(start: int) -> tuple[int, int]:
        visited = {start}
        queue = [(start, 0)]
        farthest_node = start
        max_distance = 0
        while queue:
            node, distance = queue.pop(0)
            if distance > max_distance:
                max_distance = distance
                farthest_node = node
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
        return farthest_node, max_distance

    start_node = next(iter(adj))
    farthest_node, _ = bfs(start_node)
    _, diameter = bfs(farthest_node)

    # If diameter is 1, all nodes must have the same color
    if diameter == 1:
        return k if n > 1 else 1

    # Dynamic programming to count the number of valid colorings
    @lru_cache(None)
    def dp(node: int, parent: int, color: int) -> int:
        result = 1
        for neighbor in adj[node]:
            if neighbor != parent:
                result *= sum(dp(neighbor, node, c) for c in range(k)) % MOD
        return result

    # Since the tree is a path, we can simplify the DP
    if diameter == n - 1:
        # The tree is a path, so we can color it in k * (k-1)^(n-2) ways
        return k * pow(k - 1, n - 2, MOD) % MOD

    # General case for trees with diameter < n-1
    # We need to consider all possible colorings where the path between any two nodes of the same color is monochromatic
    # This is equivalent to counting the number of ways to color the tree such that no two adjacent nodes have the same color
    # except for the nodes on the diameter, which can have the same color.

    # However, given the constraints (n, k ≤ 50), we can use a more straightforward approach:
    # We can consider the tree as a path with some additional nodes attached to it.
    # The number of ways to color the tree is the product of the number of ways to color the path and the number of ways to color the attached nodes.

    # For simplicity, we will use the following approach:
    # 1. Find the diameter path.
    # 2. Color the diameter path in k * (k-1)^(diameter-1) ways.
    # 3. For each node not on the diameter, color it with any color that is not the color of its parent.

    # Find the diameter path
    def find_diameter_path(start: int) -> list[int]:
        visited = {start}
        queue = [(start, 0, [])]
        path = []
        while queue:
            node, distance, current_path = queue.pop(0)
            current_path.append(node)
            if distance == diameter:
                path = current_path
                break
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1, current_path.copy()))
        return path

    diameter_path = find_diameter_path(farthest_node)

    # Color the diameter path
    ways = k * pow(k - 1, len(diameter_path) - 2, MOD) % MOD

    # Color the remaining nodes
    for node in adj:
        if node not in diameter_path:
            parent = next(neighbor for neighbor in adj[node] if neighbor in diameter_path)
            ways *= (k - 1) % MOD

    return ways % MOD

def main() -> None:
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    for _ in range(T):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        edges = []
        for _ in range(n - 1):
            u = int(data[idx])
            v = int(data[idx + 1])
            edges.append((u, v))
            idx += 2
        print(solve(n, k, edges))

# Uncomment the following line to run the main function
# main()
```