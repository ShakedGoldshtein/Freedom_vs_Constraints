```python
def count_connected_components(n: int, elements: list[int]) -> int:
    """
    Counts the number of connected components in a graph where nodes are connected if their bitwise AND is zero.
    Nodes are integers from the given set, with values between 0 and 2^n - 1.

    Args:
        n: The number of bits (0 ≤ n ≤ 22).
        elements: A list of distinct integers (0 ≤ a_i < 2^n).

    Returns:
        The number of connected components in the graph.
    """
    if n < 0 or n > 22:
        raise ValueError("n must be between 0 and 22")
    if not elements:
        return 0
    if any(a < 0 or a >= (1 << n) for a in elements):
        raise ValueError("All elements must be between 0 and 2^n - 1")

    max_mask = (1 << n) - 1
    elements = list(set(elements))  # Ensure uniqueness (though problem states they are distinct)
    element_to_index = {a: i for i, a in enumerate(elements)}
    parent = list(range(len(elements)))

    def find(u: int) -> int:
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u: int, v: int) -> None:
        u_root = find(u)
        v_root = find(v)
        if u_root != v_root:
            parent[v_root] = u_root

    for i, a in enumerate(elements):
        for j in range(i + 1, len(elements)):
            b = elements[j]
            if (a & b) == 0:
                union(i, j)

    unique_roots = set()
    for i in range(len(elements)):
        unique_roots.add(find(i))

    return len(unique_roots)
```