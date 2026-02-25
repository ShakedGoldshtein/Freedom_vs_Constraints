```python
from collections import defaultdict


def build_tree(n: int, edges: list[tuple[int, int]]) -> defaultdict:
    """
    Builds an adjacency list representation of the tree.

    Args:
        n (int): Number of vertices in the tree.
        edges (list of tuples): List of edges where each edge is a tuple (a, b).

    Returns:
        defaultdict: Adjacency list representation of the tree.
    """
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    return tree


def dfs(
    tree: defaultdict,
    values: list[int],
    visited: set,
    current: int,
    parent: int,
    moves: list[int],
) -> None:
    """
    Performs a depth-first search to calculate the number of moves required for each subtree.

    Args:
        tree (defaultdict): Adjacency list representation of the tree.
        values (list): List of values written on each vertex.
        visited (set): Set of visited vertices to avoid revisiting.
        current (int): Current vertex being processed.
        parent (int): Parent vertex of the current vertex.
        moves (list): List to store the number of moves required for each subtree.
    """
    visited.add(current)
    total_moves = values[current - 1]
    for neighbor in tree[current]:
        if neighbor != parent and neighbor not in visited:
            dfs(tree, values, visited, neighbor, current, moves)
            total_moves += moves[-1]
    moves.append(total_moves)


def solve(n: int, edges: list[tuple[int, int]], values: list[int]) -> int:
    """
    Calculates the minimum number of moves required to make all vertex values zero.

    Args:
        n (int): Number of vertices in the tree.
        edges (list of tuples): List of edges where each edge is a tuple (a, b).
        values (list): List of values written on each vertex.

    Returns:
        int: Minimum number of moves required.
    """
    if n == 0:
        return 0

    tree = build_tree(n, edges)
    visited = set()
    moves = []
    dfs(tree, values, visited, 1, -1, moves)
    return abs(moves[-1]) + sum(abs(x) for x in values[1:])
```