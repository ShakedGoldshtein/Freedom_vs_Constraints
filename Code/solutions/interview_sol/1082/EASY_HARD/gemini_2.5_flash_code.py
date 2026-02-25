```python
import collections

def solve(N, initial_sweetness_values, edges, Q_queries):
    """
    Solves the problem using Heavy-Light Decomposition (HLD) and a Segment Tree.
    This approach efficiently handles point updates on node sweetness and
    path sum queries from the root to any node in a tree.

    Args:
        N (int): The number of nodes in the tree (1 to N).
        initial_sweetness_values (list): A list of N integers representing the initial
                                        sweetness of apples on nodes 1 to N.
                                        (sweetness_values[0] for node 1, etc.)
        edges (list): A list of N-1 tuples, each containing two integers (N1, N2)
                      representing connected nodes.
        Q_queries (list): A list of queries. Each query is a list:
                          - Type 1: [1, ending_node] (calculate total sweetness to ending_node)
                          - Type 2: [2, node, new_sweetness] (change sweetness of a node)

    Returns:
        list: A list of integers, where each element is the total sweetness
              for a type 1 query, in the order they appear.
    """

    # HLD data structures (1-indexed for nodes 1 to N)
    N_nodes = N + 1 
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    sz = [0] * N_nodes        # Subtree size of node u
    depth = [0] * N_nodes     # Depth of node u (root is at depth 0)
    parent = [0] * N_nodes    # Parent of node u

    head = [0] * N_nodes      # Head of the heavy path containing node u
    pos = [0] * N_nodes       # Position of node u in the flattened base_array
    current_pos_idx = 0       # Current index for flattening the tree (0 to N-1)
    base_array = [0] * N      # Stores sweetness values mapped by their 'pos' index
    heavy_child = [0] * N_nodes # Heavy child of node u (child with largest subtree size)

    # DFS1: Computes subtree sizes, depths, parents, and identifies heavy children.
    # This prepares the tree structure for HLD.
    def dfs1(u, p, d):
        sz[u] = 1
        parent[u] = p
        depth[u] = d
        max_subtree_size = 0
        for v in adj[u]:
            if v == p: continue
            dfs1(v, u, d + 1)
            sz[u] += sz[v]
            if sz[v] > max_subtree_size:
                max_subtree_size = sz[v]
                heavy_child[u] = v

    # DFS2: Performs the HLD decomposition.
    # It flattens the tree into `base_array` by placing nodes of heavy paths contiguously.
    # Sets `head[u]` (head of heavy path for u) and `pos[u]` (index in `base_array`).
    def dfs2(u, p, h):
        nonlocal current_pos_idx
        head[u] = h
        pos[u] = current_pos_idx
        # `initial_sweetness_values` is 0-indexed, nodes are 1-indexed.
        base_array[current_pos_idx] = initial_sweetness_values[u - 1] 
        current_pos_idx += 1

        if heavy_child[u] != 0: # If u has a heavy child, continue the current heavy path
            dfs2(heavy_child[u], u, h)

        for v in adj[u]: # For light children, start a new heavy path
            if v == p or v == heavy_child[u]: continue
            dfs2(v, u, v) # `v` becomes the new head of its heavy path

    # Segment Tree implementation for point updates and range sum queries
    # `segment_tree` array stores the sum of values in its range.
    # Size `4 * N` is a common safe upper bound for segment tree arrays.
    segment_tree = [0] * (4 * N) 
    
    # Builds the segment tree recursively from the `base_array`.
    def build_segment_tree(node_idx, start, end):
        if start == end:
            segment_tree[node_idx] = base_array[start]
        else:
            mid = (start + end) // 2
            build_segment_tree(2 * node_idx, start, mid)
            build_segment_tree(2 * node_idx + 1, mid + 1, end)
            segment_tree[node_idx] = segment_tree[2 * node_idx] + segment_tree[2 * node_idx + 1]

    # Updates the value at a specific index `idx` in the `base_array` (and thus segment tree).
    def update_segment_tree(node_idx, start, end, idx, val):
        if start == end:
            segment_tree[node_idx] = val
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                update_segment_tree(2 * node_idx, start, mid, idx, val)
            else:
                update_segment_tree(2 * node_idx + 1, mid + 1, end, idx, val)
            segment_tree[node_idx] = segment_tree[2 * node_idx] + segment_tree[2 * node_idx + 1]

    # Queries the sum of values in a range `[l, r]` in the `base_array` using the segment tree.
    def query_segment_tree(node_idx, start, end, l, r):
        # If the query range is outside the current segment tree node's range
        if r < start or end < l:
            return 0
        # If the current segment tree node's range is completely within the query range
        if l <= start and end <= r:
            return segment_tree[node_idx]
        # Otherwise, the ranges partially overlap, so recurse on children
        mid = (start + end) // 2
        p1 = query_segment_tree(2 * node_idx, start, mid, l, r)
        p2 = query_segment_tree(2 * node_idx + 1, mid + 1, end, l, r)
        return p1 + p2

    # Calculates the sum of sweetness values along the unique path from node `u` to node `v`.
    # Assumes `u` is an ancestor of `v` (in this problem, `u` is always the root, node 1).
    def get_path_sum_hld(u, v):
        path_sum = 0
        while head[u] != head[v]: # While `u` and `v` are on different heavy paths
            # Add the sum of the heavy path segment from `head[v]` to `v`
            path_sum += query_segment_tree(1, 0, N - 1, pos[head[v]], pos[v])
            v = parent[head[v]] # Move `v` up to the parent of its heavy path's head
        
        # Now `u` and `v` are on the same heavy path.
        # Add the sum of the segment from `u` to `v` on this heavy path.
        # Since `u` is an ancestor of `v`, `pos[u]` will be less than or equal to `pos[v]`.
        path_sum += query_segment_tree(1, 0, N - 1, pos[u], pos[v])
        return path_sum

    # --- HLD Pre-processing steps ---
    # 1. Perform DFS1 starting from root (node 1), parent is 0 (sentinel), depth is 0.
    dfs1(1, 0, 0)
    # 2. Perform DFS2 starting from root (node 1), parent is 0, head of root's path is 1.
    dfs2(1, 0, 1) 
    # 3. Build the segment tree using the flattened `base_array`.
    build_segment_tree(1, 0, N - 1) 

    # --- Process queries ---
    results = []
    for query_type, *query_params in Q_queries:
        if query_type == 1:
            ending_node = query_params[0]
            # Calculate path sum from root (node 1) to the `ending_node`.
            current_sum = get_path_sum_hld(1, ending_node)
            results.append(current_sum)
        elif query_type == 2:
            node_to_update, new_sweetness = query_params
            # Update the sweetness of `node_to_update` in the segment tree.
            # `pos[node_to_update]` gives its index in the `base_array`.
            update_segment_tree(1, 0, N - 1, pos[node_to_update], new_sweetness)
    
    return results

```