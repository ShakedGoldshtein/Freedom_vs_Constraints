```python
def count_connected_components(n, m, elements):
    if m == 0:
        return 0

    mask = (1 << n) - 1
    parent = {x: x for x in elements}

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root != v_root:
            parent[v_root] = u_root

    for x in elements:
        for y in elements:
            if x == y:
                continue
            if (x & y) == 0:
                union(x, y)

    components = set()
    for x in elements:
        components.add(find(x))

    return len(components)
```