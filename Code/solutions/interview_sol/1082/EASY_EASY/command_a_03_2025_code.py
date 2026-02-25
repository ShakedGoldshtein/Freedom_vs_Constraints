```python
from collections import defaultdict


class TreeNode:
    def __init__(self, sweetness: int):
        self.sweetness = sweetness
        self.children = []


def build_tree(n: int, sweetness: list[int], edges: list[tuple[int, int]]) -> TreeNode:
    """
    Builds a tree from the given nodes, sweetness values, and edges.

    Args:
        n (int): Number of nodes in the tree.
        sweetness (list[int]): List of sweetness values for each node.
        edges (list[tuple[int, int]]): List of edges connecting nodes.

    Returns:
        TreeNode: The root node of the constructed tree.
    """
    nodes = {i + 1: TreeNode(sweetness[i]) for i in range(n)}
    for u, v in edges:
        nodes[u].children.append(nodes[v])
        nodes[v].children.append(nodes[u])
    return nodes[1]


def dfs(node: TreeNode, visited: set[TreeNode]) -> int:
    """
    Performs a Depth-First Search (DFS) to calculate the total sweetness of apples
    that can be collected from the given node downwards.

    Args:
        node (TreeNode): The current node being visited.
        visited (set[TreeNode]): A set to keep track of visited nodes to avoid cycles.

    Returns:
        int: The total sweetness of apples collected from the current node downwards.
    """
    if node in visited:
        return 0
    visited.add(node)
    total = node.sweetness
    for child in node.children:
        if child not in visited:
            total += dfs(child, visited)
    return total


def solve(
    n: int,
    sweetness: list[int],
    edges: list[tuple[int, int]],
    q: int,
    queries: list[tuple[int, int] | tuple[int, int, int]],
) -> list[int]:
    """
    Solves the problem by processing the queries on the tree.

    Args:
        n (int): Number of nodes in the tree.
        sweetness (list[int]): List of sweetness values for each node.
        edges (list[tuple[int, int]]): List of edges connecting nodes.
        q (int): Number of queries.
        queries (list[tuple[int, int] | tuple[int, int, int]]): List of queries to process.

    Returns:
        list[int]: A list of results for each query of type 1.
    """
    root = build_tree(n, sweetness, edges)
    results = []
    for query in queries:
        if query[0] == 1:
            node_id = query[1]
            node = root
            stack = [node]
            while stack:
                current = stack.pop()
                if current.sweetness == sweetness[node_id - 1]:
                    node = current
                    break
                stack.extend(current.children)
            visited = set()
            total = dfs(node, visited)
            results.append(total)
        elif query[0] == 2:
            node_id, new_sweetness = query[1], query[2]
            node = root
            stack = [node]
            while stack:
                current = stack.pop()
                if current.sweetness == sweetness[node_id - 1]:
                    node = current
                    break
                stack.extend(current.children)
            node.sweetness = new_sweetness
            sweetness[node_id - 1] = new_sweetness
    return results
```