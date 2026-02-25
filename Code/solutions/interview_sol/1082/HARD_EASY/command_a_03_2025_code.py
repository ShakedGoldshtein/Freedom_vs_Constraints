```python
from collections import defaultdict, deque


class TreeNode:
    """Represents a node in the tree with its sweetness value and connections."""

    def __init__(self, sweetness: int):
        self.sweetness = sweetness
        self.connections = []


def build_tree(n: int, sweetness: list[int], edges: list[tuple[int, int]]) -> list[TreeNode]:
    """
    Builds the tree structure from the given nodes, sweetness values, and edges.

    Args:
        n (int): Number of nodes in the tree.
        sweetness (list[int]): List of sweetness values for each node.
        edges (list[tuple[int, int]]): List of tuples representing edges between nodes.

    Returns:
        list[TreeNode]: List of TreeNode objects representing the tree.
    """
    tree = [TreeNode(s) for s in sweetness]
    for u, v in edges:
        tree[u - 1].connections.append(v - 1)
        tree[v - 1].connections.append(u - 1)
    return tree


def bfs_paths(tree: list[TreeNode]) -> dict[int, list[int]]:
    """
    Performs BFS to find all paths from the root to each node.

    Args:
        tree (list[TreeNode]): List of TreeNode objects representing the tree.

    Returns:
        dict[int, list[int]]: Dictionary mapping each node to its path from the root.
    """
    paths = defaultdict(list)
    visited = set()
    queue = deque([(0, [0])])  # (node, path)

    while queue:
        node, path = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        paths[node] = path
        for neighbor in tree[node].connections:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return paths


def preprocess(tree: list[TreeNode], paths: dict[int, list[int]]) -> dict[int, int]:
    """
    Preprocesses the tree to calculate the total sweetness for each node.

    Args:
        tree (list[TreeNode]): List of TreeNode objects representing the tree.
        paths (dict[int, list[int]]): Dictionary mapping each node to its path from the root.

    Returns:
        dict[int, int]: Dictionary mapping each node to its total sweetness.
    """
    dp = {}
    for node in range(len(tree)):
        path = paths[node]
        total = 0
        for p in path:
            total += tree[p].sweetness
        dp[node] = total
    return dp


def solve(
    n: int,
    sweetness: list[int],
    edges: list[tuple[int, int]],
    queries: list[tuple[int, int] | tuple[int, int, int]],
) -> list[int]:
    """
    Solves the problem by processing the queries on the tree.

    Args:
        n (int): Number of nodes in the tree.
        sweetness (list[int]): List of sweetness values for each node.
        edges (list[tuple[int, int]]): List of tuples representing edges between nodes.
        queries (list[tuple[int, int] | tuple[int, int, int]]): List of queries to process.

    Returns:
        list[int]: List of results for each query of type 1.
    """
    tree = build_tree(n, sweetness, edges)
    paths = bfs_paths(tree)
    dp = preprocess(tree, paths)

    results = []
    for query in queries:
        if query[0] == 1:
            node = query[1] - 1
            results.append(dp[node])
        elif query[0] == 2:
            node = query[1] - 1
            new_sweetness = query[2]
            old_sweetness = tree[node].sweetness
            tree[node].sweetness = new_sweetness
            # Update dp for all nodes that pass through this node
            for key in dp:
                if node in paths[key]:
                    dp[key] += new_sweetness - old_sweetness
    return results
```