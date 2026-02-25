```python
from collections import defaultdict

def solve(N, sweetness, edges, Q, queries):
    # Build the tree adjacency list
    tree = defaultdict(list)
    for n1, n2 in edges:
        tree[n1].append(n2)
        tree[n2].append(n1)

    # Precompute parent and children for each node (BFS to establish parent-child relationships)
    parent = [0] * (N + 1)
    children = defaultdict(list)
    visited = [False] * (N + 1)
    stack = [1]
    visited[1] = True

    while stack:
        node = stack.pop()
        for neighbor in tree[node]:
            if not visited[neighbor]:
                parent[neighbor] = node
                children[node].append(neighbor)
                visited[neighbor] = True
                stack.append(neighbor)

    # Precompute the path from root to each node
    paths = [[] for _ in range(N + 1)]
    for node in range(1, N + 1):
        current = node
        path = []
        while current != 0:
            path.append(current)
            current = parent[current]
        paths[node] = path[::-1]  # Reverse to get root-to-node path

    # Initialize a dictionary to store the sweetness values (1-based indexing)
    sweetness_dict = {i + 1: val for i, val in enumerate(sweetness)}

    # Process queries
    output = []
    for query in queries:
        if query[0] == 1:
            # Query type 1: Calculate total sweetness from root to node
            node = query[1]
            total = 0
            for n in paths[node]:
                total += sweetness_dict[n]
            output.append(total)
        elif query[0] == 2:
            # Query type 2: Update sweetness of a node
            node, new_sweetness = query[1], query[2]
            sweetness_dict[node] = new_sweetness

    return output
```