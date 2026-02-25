```python
def determine_winner(N, L, strings):
    from collections import defaultdict

    trie = defaultdict(dict)
    total_nodes = 0
    max_depth = 0

    for s in strings:
        current = trie
        for c in s:
            if c not in current:
                current[c] = defaultdict(dict)
                total_nodes += 1
            current = current[c]
        if None not in current:
            current[None] = True
            total_nodes += 1
        max_depth = max(max_depth, len(s))

    def count_possible_nodes(node, depth):
        if None in node:
            return 0
        if depth >= L:
            return 0
        count = 0
        for c in ['0', '1']:
            if c not in node:
                count += 1
            else:
                count += count_possible_nodes(node[c], depth + 1)
        return count

    possible_moves = count_possible_nodes(trie, 0)

    return "Alice" if possible_moves % 2 == 1 else "Bob"
```