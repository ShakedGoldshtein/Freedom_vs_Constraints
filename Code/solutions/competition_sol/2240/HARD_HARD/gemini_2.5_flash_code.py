```python
import collections

def solve(n: int, edges: list[tuple[int, int]], v_values: list[int]) -> int:
    """
    Calculates the minimum number of moves required to make all vertex values zero.

    An operation consists of selecting a subtree that includes vertex 1
    and increasing/decreasing all integers on its vertices by one.

    The problem can be modeled as follows: for each node `u`, we need to determine
    the net number of 'increase' operations (inc_u) and 'decrease' operations (dec_u)
    that are initiated *at node u*. An operation initiated at `u` means it affects
    `u` and all its descendants. Crucially, because any chosen subtree must
    include vertex 1, these operations also implicitly propagate upwards from `u`
    to its parent, grandparent, all the way to root 1.

    The final value of any node `x` will be its initial value plus the net effect
    of all operations that apply to it. This net effect is the sum of (inc_y - dec_y)
    for all nodes `y` on the path from 1 to `x` (inclusive). We want this final value
    to be 0 for all nodes `x`.
    The total number of moves is the sum of (inc_y + dec_y) for all nodes `y` across the tree.

    This can be solved using a Depth-First Search (DFS) from the root (vertex 1).
    For each node `u`, the DFS function calculates the net increase and decrease
    operations that must be applied at `u` to satisfy `u` and its entire
    subtree (considering the values from its children's subtrees). These operations
    are accumulated into global counters (`total_inc_ops`, `total_dec_ops`)
    and also returned to `u`'s parent, as they affect `u`'s parent's value as well.

    Args:
        n: The number of vertices in the tree (1 <= n <= 10^5).
        edges: A list of (u, v) tuples representing edges in the tree.
               Vertices are 1-indexed (1 <= u, v <= n; u != v).
               Guaranteed that the input graph is a tree.
        v_values: A list of n integers, where v_values[i] is the initial
                  value of vertex (i+1) (|v_i| <= 10^9).

    Returns:
        The minimum total number of operations (sum of all increase and decrease moves).
    """

    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    total_inc_ops = 0  # Global counter for total increase operations across all nodes
    total_dec_ops = 0  # Global counter for total decrease operations across all nodes

    def dfs(u: int, p: int) -> tuple[int, int]:
        """
        Performs a DFS traversal from node `u` to calculate operations needed
        within its subtree and propagate requirements upwards.

        Args:
            u: The current vertex (1-indexed).
            p: The parent of the current vertex (1-indexed, or 0 for dummy parent of root).

        Returns:
            A tuple (net_increases_to_propagate, net_decreases_to_propagate).
            These represent the total net increase and decrease operations that
            either originated at `u` or propagated through `u` from its children's
            subtrees, and thus must be accounted for by `u`'s parent (`p`)
            and its ancestors.
        """
        nonlocal total_inc_ops, total_dec_ops

        child_net_increase_sum = 0  # Sum of increases propagating up from children's subtrees
        child_net_decrease_sum = 0  # Sum of decreases propagating up from children's subtrees

        for v in adj[u]:
            if v == p:
                continue
            
            # Recursively call DFS for children
            inc_from_child_subtree, dec_from_child_subtree = dfs(v, u)
            
            # Accumulate operations that originate in child's subtree and must
            # propagate upwards through `u` to `p` (and eventually to root 1).
            child_net_increase_sum += inc_from_child_subtree
            child_net_decrease_sum += dec_from_child_subtree

        # Calculate the effective value at node `u`.
        # This value is `u`'s initial value, adjusted by the net effect of operations
        # that originated in its children's subtrees and have propagated up to `u`.
        # `v_values` is 0-indexed, so `v_values[u-1]` for 1-indexed vertex `u`.
        current_effective_value = v_values[u-1] + child_net_increase_sum - child_net_decrease_sum

        # Determine how many new increase/decrease operations need to be
        # initiated *at node `u` itself* to make its `current_effective_value` zero.
        # These new operations will affect `u` and its entire subtree,
        # and also propagate upwards to `parent(u)` and eventually to root 1.
        inc_ops_initiated_at_u = 0
        dec_ops_initiated_at_u = 0

        if current_effective_value > 0:
            dec_ops_initiated_at_u = current_effective_value
        elif current_effective_value < 0:
            inc_ops_initiated_at_u = -current_effective_value
        
        # Add these newly determined operations to the global total.
        total_inc_ops += inc_ops_initiated_at_u
        total_dec_ops += dec_ops_initiated_at_u

        # Return the net operations that need to be accounted for by parent `p`.
        # This is the sum of operations newly initiated at `u` (inc_ops_initiated_at_u, dec_ops_initiated_at_u)
        # and those that propagated through `u` from its children's subtrees
        # (child_net_increase_sum, child_net_decrease_sum).
        return (inc_ops_initiated_at_u + child_net_increase_sum,
                dec_ops_initiated_at_u + child_net_decrease_sum)
    
    # Start the DFS from vertex 1 (the root), with 0 as a dummy parent.
    dfs(1, 0)

    # The total minimum operations is the sum of all accumulated increases and decreases
    # initiated at any node in the tree.
    return total_inc_ops + total_dec_ops

```