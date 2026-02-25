```python
MOD = 10**9 + 7

def solve(n: int, k: int, edges: list[tuple[int, int]]) -> int:
    """
    Calculate the number of ways to color a tree with n vertices using k colors,
    such that all vertices on any path between two vertices of the same color are also colored with the same color.

    Args:
        n (int): Number of vertices in the tree.
        k (int): Number of available colors.
        edges (list of tuples): List of edges in the tree, where each edge is represented as a tuple (u, v).

    Returns:
        int: The number of valid colorings modulo 10^9 + 7.
    """
    from collections import defaultdict

    # Build adjacency list representation of the tree
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Function to calculate the number of ways to color the tree
    def dfs(node: int, parent: int) -> list[int]:
        """
        Perform a depth-first search to calculate the number of ways to color the subtree rooted at `node`.

        Args:
            node (int): Current node being processed.
            parent (int): Parent node of the current node.

        Returns:
            list of int: A list where the i-th element represents the number of ways to color the subtree
                         rooted at `node` such that `node` is colored with color i.
        """
        ways = [0] * k
        for child in tree[node]:
            if child != parent:
                child_ways = dfs(child, node)
                new_ways = [0] * k
                for i in range(k):
                    for j in range(k):
                        # If the current node and child node have the same color,
                        # all vertices in the path between them must have the same color.
                        # Therefore, we only consider the case where i == j.
                        if i == j:
                            new_ways[i] = (new_ways[i] + ways[i] * child_ways[j]) % MOD
                ways = new_ways
        for i in range(k):
            ways[i] = (ways[i] + 1) % MOD  # Add 1 for the current node's color
        return ways

    # Start DFS from any node (e.g., node 1)
    result = dfs(1, -1)
    total = sum(result) % MOD
    return total

def main() -> list[int]:
    """
    Main function to handle multiple test cases and compute the results.

    Returns:
        list of int: A list containing the results for each test case.
    """
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
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
        results.append(solve(n, k, edges))
    return results

# Example usage:
# results = main()
# for result in results:
#     print(result)
```