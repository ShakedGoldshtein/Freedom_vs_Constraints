```python
def solve(n: int, m: int, numbers: list[int]) -> int:
    """
    Counts the number of connected components in a graph where nodes are connected if their bitwise AND is zero.

    Args:
        n (int): The maximum number of bits in the integers (0 <= n <= 22).
        m (int): The number of integers in the set (1 <= m <= 2^n).
        numbers (list[int]): A list of distinct integers in the set (0 <= a_i < 2^n).

    Returns:
        int: The number of connected components in the graph.
    """

    def find(parent: list[int], x: int) -> int:
        """
        Finds the root of the set containing x with path compression.

        Args:
            parent (list[int]): A list representing the parent of each node.
            x (int): The node to find the root for.

        Returns:
            int: The root of the set containing x.
        """
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent: list[int], rank: list[int], x: int, y: int) -> None:
        """
        Unions the sets containing x and y using union by rank.

        Args:
            parent (list[int]): A list representing the parent of each node.
            rank (list[int]): A list representing the rank of each node.
            x (int): The first node to union.
            y (int): The second node to union.
        """
        xroot = find(parent, x)
        yroot = find(parent, y)
        if xroot == yroot:
            return
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        else:
            parent[yroot] = xroot
            if rank[xroot] == rank[yroot]:
                rank[xroot] += 1

    # Initialize parent and rank arrays for Union-Find
    parent = list(range(m))
    rank = [0] * m

    # Iterate over all pairs of numbers to find connected components
    for i in range(m):
        for j in range(i + 1, m):
            if (numbers[i] & numbers[j]) == 0:
                union(parent, rank, i, j)

    # Count the number of unique roots (connected components)
    components = set()
    for i in range(m):
        components.add(find(parent, i))

    return len(components)
```