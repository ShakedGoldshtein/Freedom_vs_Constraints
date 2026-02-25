```python
import sys

# Setting a higher recursion limit for potentially deep trees.
# For N=10^4, the tree depth can be up to N, requiring N recursion depth.
sys.setrecursionlimit(2 * 10**5)

class SegmentTree:
    """
    Segment Tree for range sum queries and point updates.
    Supports 1-indexed operations for use with Heavy-Light Decomposition.
    """
    def __init__(self, arr, n_elements):
        """
        Initializes the Segment Tree.

        Args:
            arr (list): The 1-indexed base array for the tree (stores values at leaves).
                        `arr[0]` is unused. `arr[1]` to `arr[n_elements]` contain data.
            n_elements (int): The number of actual elements in the base array (size of the effective data, from index 1 to n_elements).
        """
        self.n = n_elements
        # The tree array requires about 4*N space for a segment tree.
        self.tree = [0] * (4 * self.n)
        self._arr = arr  # Reference to the base_array for initial build
        self._build(1, 1, self.n)

    def _build(self, tree_idx, start, end):
        """
        Recursively builds the segment tree.
        """
        if start == end:
            # Leaf node: store the value from the base array
            self.tree[tree_idx] = self._arr[start]
        else:
            mid = (start + end) // 2
            # Recursively build left and right children
            self._build(2 * tree_idx, start, mid)
            self._build(2 * tree_idx + 1, mid + 1, end)
            # Internal node: sum of its children
            self.tree[tree_idx] = self.tree[2 * tree_idx] + self.tree[2 * tree_idx + 1]

    def update(self, idx, val):
        """
        Updates the value at original array index 'idx' to 'val'.
        Time Complexity: O(log N).

        Args:
            idx (int): The 1-indexed position in the base array to update.
            val (int): The new value to set.
        """
        self._update(1, 1, self.n, idx, val)

    def _update(self, tree_idx, start, end, idx, val):
        """
        Recursive helper for updating a point in the segment tree.
        """
        if start == end:
            # Leaf node reached: update its value
            self.tree[tree_idx] = val
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                # Update in the left child's segment
                self._update(2 * tree_idx, start, mid, idx, val)
            else:
                # Update in the right child's segment
                self._update(2 * tree_idx + 1, mid + 1, end, idx, val)
            # Update current node's value as sum of its children
            self.tree[tree_idx] = self.tree[2 * tree_idx] + self.tree[2 * tree_idx + 1]

    def query_range(self, L, R):
        """
        Queries the sum of values in the range [L, R] in the original array.
        Time Complexity: O(log N).

        Args:
            L (int): The 1-indexed start of the query range.
            R (int): The 1-indexed end of the query range.

        Returns:
            int: The sum of values in the specified range. Returns 0 if L > R (invalid range).
        """
        if L > R:  # Handle invalid range
            return 0
        return self._query(1, 1, self.n, L, R)

    def _query(self, tree_idx, start, end, L, R):
        """
        Recursive helper for querying a range in the segment tree.
        """
        # If the current segment is completely outside the query range
        if R < start or end < L:
            return 0
        # If the current segment is completely within the query range
        if L <= start and end <= R:
            return self.tree[tree_idx]

        # Partially overlapping segment: recurse on children
        mid = (start + end) // 2
        p1 = self._query(2 * tree_idx, start, mid, L, R)
        p2 = self._query(2 * tree_idx + 1, mid + 1, end, L, R)
        return p1 + p2


def solve_jaggu_monkey(num_nodes, initial_sweetness_input, edges_input, num_queries, queries_input):
    """
    Solves the Jaggu monkey problem using Heavy-Light Decomposition (HLD) and a Segment Tree.
    This approach efficiently handles point updates on node values and path sum queries
    from the root to any given node in a tree.

    Time Complexity:
        - HLD Precomputation (DFS1, DFS2): O(N)
        - Segment Tree Build: O(N)
        - Type 1 Query (Path Sum): O(log^2 N)
        - Type 2 Query (Point Update): O(log N)
        Total: O(N + Q * log^2 N) where N is num_nodes and Q is num_queries.
        With N, Q <= 10^4, this is approximately 10^4 + 10^4 * (14)^2 = 10^4 + 10^4 * 196 = ~2 * 10^6 operations, which is efficient.

    Space Complexity: O(N) for adjacency lists, HLD arrays, and Segment Tree.

    Args:
        num_nodes (int): The total number of nodes in the tree (1 to N).
        initial_sweetness_input (list): A list of N integers representing the initial sweetness of apples
                                        on nodes 1 to N. Node 1 corresponds to `initial_sweetness_input[0]`, etc.
        edges_input (list of tuples): A list of (N1, N2) tuples representing connected nodes.
        num_queries (int): The total number of queries.
        queries_input (list of lists): A list of queries. Each query is formatted as:
                                       - [1, node_id] for a type 1 query (get total sweetness to node_id).
                                       - [2, node_id, new_sweetness] for a type 2 query (update node_id's sweetness).

    Returns:
        list: A list of total sweetness values for each query of type 1, in the order they were processed.
    """
    if num_nodes == 0:
        return []

    # Adjacency list for the tree, initially undirected. Node IDs are 1-indexed.
    adj = [[] for _ in range(num_nodes + 1)]
    for u, v in edges_input:
        adj[u].append(v)
        adj[v].append(u)

    # current_sweetness stores the latest sweetness value for each node (1-indexed).
    # We create a mutable copy from the input list.
    current_sweetness = [0] + list(initial_sweetness_input) 

    # HLD specific arrays, 1-indexed for nodes.
    parent = [0] * (num_nodes + 1)         # parent[u] stores the parent of node u.
    depth = [0] * (num_nodes + 1)          # depth[u] stores the depth of node u (root at depth 0).
    subtree_size = [0] * (num_nodes + 1)   # subtree_size[u] stores the number of nodes in u's subtree.
    heavy_child = [0] * (num_nodes + 1)    # heavy_child[u] stores the heavy child of u (0 if no heavy child).
    head = [0] * (num_nodes + 1)           # head[u] stores the head node of the heavy path containing u.
    pos_in_base_array = [0] * (num_nodes + 1) # pos_in_base_array[u] stores u's 1-indexed position in the Segment Tree's flattened array.

    # Base array for the Segment Tree, populated during DFS2. 1-indexed.
    base_array = [0] * (num_nodes + 1) 
    
    # global_pos_timer is a global counter to assign unique positions in `base_array`.
    global_pos_timer = 0 

    def dfs1(u, p, d):
        """
        First DFS pass: Calculates parent, depth, subtree_size, and identifies the heavy child for each node.
        This effectively transforms the undirected graph into a rooted tree structure.

        Args:
            u (int): The current node being visited.
            p (int): The parent of the current node u.
            d (int): The depth of the current node u (distance from root).

        Returns:
            int: The calculated subtree size of node u.
        """
        parent[u] = p
        depth[u] = d
        subtree_size[u] = 1
        max_subtree_size = 0 # To find the heaviest child

        for v in adj[u]:
            if v == p:  # Avoid traversing back to the parent
                continue
            # Recursively call DFS1 for children and accumulate subtree sizes
            subtree_size[u] += dfs1(v, u, d + 1)
            # Identify the heavy child
            if subtree_size[v] > max_subtree_size:
                max_subtree_size = subtree_size[v]
                heavy_child[u] = v
        return subtree_size[u]

    def dfs2(u, h):
        """
        Second DFS pass: Builds HLD paths, assigns the head of heavy paths,
        and populates `pos_in_base_array` and `base_array` for the Segment Tree.
        Heavy children are processed first to keep them on the same heavy path.

        Args:
            u (int): The current node being visited.
            h (int): The head node of the heavy path that node u belongs to.
        """
        nonlocal global_pos_timer
        head[u] = h  # Assign the head of the current heavy path to node u
        global_pos_timer += 1
        pos_in_base_array[u] = global_pos_timer # Assign a unique position in the flattened array
        base_array[global_pos_timer] = current_sweetness[u] # Store current sweetness value

        if heavy_child[u] != 0:
            # Recursively process the heavy child, keeping it on the same heavy path
            dfs2(heavy_child[u], h)

        for v in adj[u]:
            # Process light children: they start new heavy paths
            if v == parent[u] or v == heavy_child[u]: # Skip parent and already processed heavy child
                continue
            dfs2(v, v) # Light child 'v' becomes the head of its own new heavy path

    # --- HLD Precomputation ---
    # Start DFS1 from root node 1. Parent is 0 (dummy), depth is 0.
    dfs1(1, 0, 0) 
    # Start DFS2 from root node 1. Its own heavy path's head is itself.
    dfs2(1, 1) 

    # Initialize the Segment Tree with the populated base_array.
    # The SegmentTree will manage num_nodes elements (from 1 to num_nodes).
    seg_tree = SegmentTree(base_array, num_nodes)

    results = [] # Stores results for type 1 queries

    # --- Process Queries ---
    for query_type, *query_params in queries_input:
        if query_type == 1:
            target_node = query_params[0]
            total_sweetness = 0
            curr_node = target_node
            root_node = 1

            # Traverse up from the target_node towards the root using HLD chains.
            # Query sum of sweetness values along heavy path segments.
            while head[curr_node] != head[root_node]: # While current node and root are not on the same heavy path
                # Add sum of sweetness values in the current heavy path segment
                total_sweetness += seg_tree.query_range(
                    pos_in_base_array[head[curr_node]], # Start position of the current heavy path segment
                    pos_in_base_array[curr_node]        # End position of the current heavy path segment
                )
                # Move to the parent of the head of the current heavy path
                curr_node = parent[head[curr_node]] 

            # At this point, curr_node and root_node are on the same heavy path.
            # Query the remaining segment from the root_node's position to curr_node's position.
            total_sweetness += seg_tree.query_range(
                pos_in_base_array[root_node], 
                pos_in_base_array[curr_node]
            )
            results.append(total_sweetness)

        elif query_type == 2:
            node_id, new_sweetness = query_params
            # Update the current sweetness value for the node
            current_sweetness[node_id] = new_sweetness 
            # Update the Segment Tree at the corresponding position
            seg_tree.update(pos_in_base_array[node_id], new_sweetness)
            
    return results
```