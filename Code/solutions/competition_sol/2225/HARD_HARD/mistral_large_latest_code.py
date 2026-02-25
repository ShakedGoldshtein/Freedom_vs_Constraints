```python
def determine_winner(N, L, strings):
    """
    Determines the winner of the game between Alice and Bob when both play optimally.

    Args:
        N (int): Number of strings in the initial good string set S.
        L (int): Maximum allowed length of any string in S.
        strings (list[str]): List of binary strings in the initial good string set S.

    Returns:
        str: "Alice" if Alice wins, "Bob" otherwise.
    """
    class TrieNode:
        __slots__ = ['children', 'is_end']
        def __init__(self):
            self.children = {}
            self.is_end = False

    root = TrieNode()
    total_nodes = 0

    def insert(s):
        nonlocal total_nodes
        node = root
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
                total_nodes += 1
            node = node.children[c]
        node.is_end = True

    def count_possible_moves():
        nonlocal total_nodes
        max_possible = 0
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if depth == L:
                continue
            if not node.is_end:
                available = 2 - len(node.children)
                if available > 0:
                    max_possible += available
            for child in node.children.values():
                stack.append((child, depth + 1))
        return max_possible

    for s in strings:
        insert(s)

    moves = count_possible_moves()
    return "Alice" if moves % 2 == 1 else "Bob"
```