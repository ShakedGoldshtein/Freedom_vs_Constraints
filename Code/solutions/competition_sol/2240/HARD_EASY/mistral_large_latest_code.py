```python
import sys
from collections import deque

def solve(n, edges, values):
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    # Build tree structure with parent pointers and depth
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]

    # BFS to set up parent and depth
    q = deque([1])
    parent[1] = 0  # 0 means no parent
    while q:
        u = q.popleft()
        for v in adj[u]:
            if parent[v] == 0 and v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                children[u].append(v)
                q.append(v)

    # Compute in and out times for Euler Tour (for LCA or subtree queries)
    in_time = [0] * (n + 1)
    out_time = [0] * (n + 1)
    time = 1

    stack = [(1, True)]
    while stack:
        u, is_first_visit = stack.pop()
        if is_first_visit:
            in_time[u] = time
            time += 1
            stack.append((u, False))
            # Push children in reverse order to process them in order
            for v in reversed(children[u]):
                stack.append((v, True))
        else:
            out_time[u] = time - 1

    # Fenwick Tree (Binary Indexed Tree) for range updates and point queries
    class FenwickTree:
        def __init__(self, size):
            self.size = size
            self.tree = [0] * (self.size + 2)

        def update_range(self, l, r, val):
            self._update_range(l, val)
            self._update_range(r + 1, -val)

        def _update_range(self, idx, val):
            while idx <= self.size:
                self.tree[idx] += val
                idx += idx & -idx

        def query_point(self, idx):
            res = 0
            while idx > 0:
                res += self.tree[idx]
                idx -= idx & -idx
            return res

    # The problem reduces to finding the minimal number of operations to make all v_i = 0,
    # where each operation is adding/subtracting 1 to all nodes in a subtree containing root (1).
    # This is equivalent to finding the minimal number of operations where each operation is
    # adding/subtracting 1 to a subtree rooted at some node (since any subtree containing root
    # is a union of subtrees rooted at children of some node in the path from root to the subtree's root).
    # However, a more efficient approach is to realize that the operations can be represented as
    # a set of increments/decrements on paths from the root to various nodes, and the problem
    # reduces to finding the minimal number of such path operations to cancel out the initial values.
    # This is similar to the problem of finding the minimal number of prefix operations to make all elements zero,
    # which can be solved by noting that the operations form a telescoping series.

    # The key observation is that the operations can be represented as a set of increments/decrements
    # on the paths from the root to the leaves, and the minimal number of operations is equal to the
    # sum of absolute differences between the values of adjacent nodes in the tree's DFS order,
    # but this is not directly applicable. Instead, we can model the problem as follows:
    # For each node, the number of operations affecting it is equal to the sum of operations on all its ancestors.
    # Let op[u] be the number of operations performed on the subtree rooted at u (which includes all its descendants).
    # Then, the final value of a node u is v[u] + sum_{ancestor w of u} op[w].
    # We need to find op[u] for all u such that this sum is zero for all nodes.
    # This can be rewritten as a system of linear equations where for each node u:
    # v[u] + sum_{w in path from root to u} op[w] = 0.
    # To solve this, we can perform a post-order traversal and compute the required op[u] for each node u.
    # Specifically, for a node u, the sum of operations on its ancestors (