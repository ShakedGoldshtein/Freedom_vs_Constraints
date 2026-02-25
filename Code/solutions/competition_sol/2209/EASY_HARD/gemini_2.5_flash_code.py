```python
import collections

def solve(n, edges):
    """
    Calculates the minimum and maximum possible values of f for a given tree.

    f is the number of distinct weights in an assignment where for every two
    different leaves v1 and v2, the bitwise XOR of weights of all edges on
    the simple path between v1 and v2 is 0. Edge weights must be positive.

    Args:
        n (int): The number of vertices in the tree.
        edges (list): A list of tuples, where each tuple (a, b) represents an
                      edge between vertex a and vertex b.

    Returns:
        tuple: A tuple containing two integers: (f_min, f_max).
    """

    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1

    leaves = []
    for i in range(1, n + 1):
        if degree[i] == 1:
            leaves.append(i)
    
    # --- Calculate f_min ---
    # f_min is 1 if all leaves have the same parity depth from an arbitrary root.
    # Otherwise, f_min is 3.

    # Find depths using BFS from node 1 (arbitrary root, guaranteed to exist as n >= 3)
    start_node = 1
    depth = [-1] * (n + 1)
    q = collections.deque([(start_node, 0)])
    depth[start_node] = 0
    visited = [False] * (n + 1)
    visited[start_node] = True

    while q:
        u, d = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = d + 1
                q.append((v, d + 1))
    
    # Check parities of leaf depths
    has_even_depth_leaf = False
    has_odd_depth_leaf = False
    for leaf_node in leaves:
        if depth[leaf_node] % 2 == 0:
            has_even_depth_leaf = True
        else:
            has_odd_depth_leaf = True
            
    if has_even_depth_leaf and has_odd_depth_leaf:
        f_min = 3
    else:
        f_min = 1
        
    # --- Calculate f_max ---
    # f_max can be achieved by assigning distinct XOR values (X_u) to each node u.
    # The condition X_v1 XOR X_v2 = 0 for leaves v1, v2 means X_v = K for all leaves v.
    # So, for an edge (l, u) where l is a leaf, w(l,u) = K XOR X_u.
    # For an edge (u, v) where u, v are internal nodes, w(u,v) = X_u XOR X_v.
    # To maximize f:
    # 1. All edges (u,v) where u,v are internal nodes can be assigned distinct weights.
    #    There are (n-1) - N_L such edges, where N_L is the number of leaves.
    # 2. For edges connected to leaves, i.e., (l,u), all edges sharing the same
    #    internal node u as parent will have the same weight (K XOR X_u).
    #    Thus, the number of distinct weights from leaf-connected edges is the
    #    number of distinct internal nodes that are adjacent to at least one leaf.
    #    Let this be C_adj_L.
    # We assume we can pick K and X_u values to make all these ( (n-1) - N_L ) + C_adj_L
    # weights distinct. This is possible using sufficiently large and well-chosen values.

    N_L = len(leaves)
    
    nodes_adj_to_leaves = set()
    for leaf_node in leaves:
        # A leaf has only one neighbor
        parent_of_leaf = adj[leaf_node][0] 
        nodes_adj_to_leaves.add(parent_of_leaf)
    
    C_adj_L = len(nodes_adj_to_leaves)
    
    f_max = (n - 1) - N_L + C_adj_L

    return f_min, f_max

```