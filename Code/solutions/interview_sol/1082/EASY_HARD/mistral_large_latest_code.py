```python
import sys
from collections import defaultdict

def solve(N, sweetness, edges, Q, queries):
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    parent = [0] * (N + 1)
    depth = [0] * (N + 1)
    stack = [(1, 0)]
    while stack:
        node, p = stack.pop()
        parent[node] = p
        for neighbor in tree[node]:
            if neighbor != p:
                depth[neighbor] = depth[node] + 1
                stack.append((neighbor, node))

    binary_lifting = [[0] * (N + 1) for _ in range(20)]
    binary_lifting[0] = parent[:]
    for k in range(1, 20):
        for v in range(1, N + 1):
            binary_lifting[k][v] = binary_lifting[k-1][binary_lifting[k-1][v]]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        for k in range(19, -1, -1):
            if depth[u] - (1 << k) >= depth[v]:
                u = binary_lifting[k][u]
        if u == v:
            return u
        for k in range(19, -1, -1):
            if binary_lifting[k][u] != binary_lifting[k][v]:
                u = binary_lifting[k][u]
                v = binary_lifting[k][v]
        return parent[u]

    def get_path(u, v):
        ancestor = lca(u, v)
        path = []
        while u != ancestor:
            path.append(u)
            u = parent[u]
        temp = []
        while v != ancestor:
            temp.append(v)
            v = parent[v]
        path.append(ancestor)
        path += temp[::-1]
        return path

    sweetness = [0] + sweetness
    res = []
    for query in queries:
        if query[0] == 1:
            node = query[1]
            path = get_path(1, node)
            total = sum(sweetness[n] for n in path)
            res.append(total)
        else:
            node, new_sweet = query[1], query[2]
            sweetness[node] = new_sweet
    return res
```