```python
import collections

MOD = 10**9 + 7

def solve_tree_coloring(n: int, k: int, edges: list[tuple[int, int]]) -> int:
    """
    Calculates the number of ways to color a tree such that for any two vertices
    of the same color, all vertices on the path joining them also have that color.

    This property is equivalent to stating that for any color `C`, the set of
    vertices colored `C` must induce a connected subgraph (a subtree).
    Furthermore, this is equivalent to: for any vertex `x`, if `color[x] != C`,
    then `x` has at most one neighbor of color `C`.

    The solution uses dynamic programming on trees.
    We define three DP states for a subtree rooted at `u`, in relation to its parent `p`:

    1. `dp_same[c_u]`: Number of ways to color the subtree rooted at `u`,
       such that `u` is colored `c_u`, and `u` IS connected upwards by color `c_u`.
       (i.e., `parent[u]` IS color `c_u`).
       In this state, for any `c_x != c_u`, `u` can have any number of neighbors of `c_x` (no 'at most one' restriction from `u`'s perspective,
       as `u` itself is `c_u`). So children can be `c_u` or any `c_x != c_u`.

    2. `dp_diff_all_ok[c_u][c_p]`: Number of ways to color the subtree rooted at `u`,
       such that `u` is colored `c_u`, `parent[u]` IS color `c_p` (`c_p != c_u`),
       and NO child `v` of `u` has a color `c_x` such that `c_x != c_u` and `c_x != c_p`.
       (i.e., all children `v` are either `c_u` or `c_x` with `c_x = c_p`, which is forbidden,
       or `c_x \ne c_u, c_p` but no such children exists yet).

    3. `dp_diff_one_conflict[c_u][c_p]`: Number of ways to color the subtree rooted at `u`,
       such that `u` is colored `c_u`, `parent[u]` IS color `c_p` (`c_p != c_u`),
       and EXACTLY ONE child `v` of `u` has a color `c_x` such that `c_x != c_u` and `c_x != c_p`.
       (This `c_x` is the "conflicting" color that `u` can have at most one neighbor of).

    Args:
        n (int): Number of vertices in the tree (1-indexed in input, converted to 0-indexed internally).
        k (int): Total number of colors available (0-indexed internally).
        edges (list): A list of tuples, where each tuple `(u, v)` represents an edge.

    Returns:
        int: The total number of valid colorings modulo 10^9 + 7.
    """

    if n == 0:
        return 0
    if n == 1:
        return k % MOD

    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    # `k_plus_1_dummy_color` is used as an index for a non-existent parent color,
    # specifically for the root node, where `c_p` constraint doesn't apply.
    k_plus_1_dummy_color = k 

    # Recursive DFS function to compute DP states
    def dfs_recursive(u: int, p: int):
        # Initialize DP states for a new node `u` (before processing its children).
        # These represent the base case: `u` itself, with no children yet considered.
        # Product-like accumulations are initialized to 1, sum-like to 0.
        current_dp_same = [1] * k
        current_dp_diff_all_ok = [[1] * (k + 1) for _ in range(k)]
        current_dp_diff_one_conflict = [[0] * (k + 1) for _ in range(k)]

        # If `u` is colored `c_u` and its parent is also `c_u`, then `u` is in a `dp_same` state.
        # This means `u` is not in a `dp_diff` state, so `current_dp_diff_all_ok[c_u][c_u]` must be 0.
        for c_val in range(k):
            current_dp_diff_all_ok[c_val][c_val] = 0

        # Iterate over children of `u`
        for v in adj[u]:
            if v == p: # Skip parent
                continue

            # Recursively call DFS for child `v`
            child_dp_same, child_dp_diff_all_ok, child_dp_diff_one_conflict = dfs_recursive(v, u)

            # Precompute `child_total_ways_if_not_cu[c_u]` for convenience:
            # For child `v`, if `u` is `c_u`, this is the total ways `v` can be colored `c_x` (`c_x != c_u`).
            # This is `sum_{c_x != c_u} (child_dp_diff_all_ok[c_x][c_u] + child_dp_diff_one_conflict[c_x][c_u])`.
            child_total_ways_if_not_cu = [0] * k
            for cu_idx in range(k): # `u`'s color
                for cx_idx in range(k): # `v`'s color
                    if cx_idx == cu_idx: continue
                    child_total_ways_if_not_cu[cu_idx] = (child_total_ways_if_not_cu[cu_idx] + 
                                                         child_dp_diff_all_ok[cx_idx][cu_idx] + 
                                                         child_dp_diff_one_conflict[cx_idx][cu_idx]) % MOD

            # Temporary DP arrays to build up results after processing child `v`
            next_dp_same = [0] * k
            next_dp_diff_all_ok = [[0] * (k + 1) for _ in range(k)]
            next_dp_diff_one_conflict = [[0] * (k + 1) for _ in range(k)]

            for c_u in range(k): # Iterate through `u`'s possible colors
                # --- Update for `dp_same[c_u]` (u is `c_u`, parent `p` is `c_u`) ---
                # For child `v`, it can either:
                #   1. Be `c_u` (match `u`'s color): `child_dp_same[c_u]` ways.
                #   2. Be `c_x \ne c_u` (not match `u`'s color): `child_total_ways_if_not_cu[c_u]` ways.
                # Total options for child `v` in this scenario: `(child_dp_same[c_u] + child_total_ways_if_not_cu[c_u])`
                val_v_for_same_state = (child_dp_same[c_u] + child_total_ways_if_not_cu[c_u]) % MOD
                next_dp_same[c_u] = (current_dp_same[c_u] * val_v_for_same_state) % MOD

                # --- Update for `dp_diff_all_ok[c_u][c_p]` and `dp_diff_one_conflict[c_u][c_p]` ---
                # Here `u` is `c_u`, and `p` is `c_p` (`c_p != c_u`).
                # We iterate `c_p` over all actual colors `0..k-1` and the dummy `k_plus_1_dummy_color`.
                for c_p in range(k + 1):
                    if c_p == c_u: # Parent cannot be same color as `u` in a `diff` state
                        continue

                    prev_all_ok_for_cu_cp = current_dp_diff_all_ok[c_u][c_p]
                    prev_one_conflict_for_cu_cp = current_dp_diff_one_conflict[c_u][c_p]

                    # `term_v_no_conflict_sum`: Ways for child `v` that do NOT introduce a new 'conflict' for `u`.
                    #   - `v` is `c_u`: `child_dp_same[c_u]` ways.
                    #   - `v` is `c_x` where `c_x \ne c_u` AND `c_x \ne c_p`: Sum of `(child_dp_diff_all_ok[c_x][c_u] + child_dp_diff_one_conflict[c_x][c_u])` for these `c_x`.
                    #     This sum is `child_total_ways_if_not_cu[c_u]` MINUS ways where `v` is `c_p` (if `c_p` is a real color).
                    term_v_no_conflict_sum = (child_dp_same[c_u] + child_total_ways_if_not_cu[c_u]) % MOD
                    if c_p != k_plus_1_dummy_color: # If `c_p` is a real color, `v` cannot be `c_p` here.
                        # We subtract ways for `v` to be `c_p`, which were included in `child_total_ways_if_not_cu`.
                        term_v_no_conflict_sum = (term_v_no_conflict_sum - 
                                                  (child_dp_diff_all_ok[c_p][c_u] + child_dp_diff_one_conflict[c_p][c_u]) % MOD + MOD) % MOD

                    # `term_v_one_conflict_sum`: Ways for child `v` that *introduce* the 'single conflict' for `u`.
                    #   - `v` must be `c_x` where `c_x \ne c_u` AND `c_x \ne c_p`.
                    #   - This term is the ways for `v` to have color `c_p` (if `c_p` is a real color), because `u` already has `p` as a neighbor of `c_p`.
                    #     If `v` also has `c_p`, that means `u` has *two* neighbors of `c_p` while `u` is not `c_p`, which is invalid.
                    # So, `term_v_one_conflict_sum` should represent `v` becoming the ONE forbidden color.
                    # This is `child_dp_diff_all_ok[c_p][c_u] + child_dp_diff_one_conflict[c_p][c_u]` if `c_p` is a real color.
                    term_v_one_conflict_sum = 0
                    if c_p != k_plus_1_dummy_color:
                        # If `c_p` is a real color, `v` cannot take this color. So `term_v_one_conflict_sum` is zero.
                        # No, `term_v_one_conflict_sum` is how many ways `v` can pick a color `c_x` that becomes the *sole* "conflicting" color.
                        # This happens if `v` takes color `c_x` such that `c_x \ne c_u` AND `c_x \ne c_p`.
                        # It is `child_total_ways_if_not_cu[c_u]` minus the `v` having `c_p` part.
                        term_v_one_conflict_sum = (child_total_ways_if_not_cu[c_u] - 
                                                  (child_dp_diff_all_ok[c_p][c_u] + child_dp_diff_one_conflict[c_p][c_u]) % MOD + MOD) % MOD
                    else: # `c_p` is dummy, meaning no color `c_p` is forbidden by parent.
                        term_v_one_conflict_sum = child_total_ways_if_not_cu[c_u]
                    
                    # For `dp_diff_all_ok[c_u][c_p]`:
                    #  1. All previous children were `all_ok`, and `v` is `no_conflict`.
                    #  2. One previous child was `one_conflict`, and `v` is `one_conflict` (this sums up to `all_ok` + `one_conflict`).
                    next_dp_diff_all_ok[c_u][c_p] = (prev_all_ok_for_cu_cp * term_v_no_conflict_sum) % MOD
                    next_dp_diff_all_ok[c_u][c_p] = (next_dp_diff_all_ok[c_u][c_p] + prev_one_conflict_for_cu_cp * term_v_one_conflict_sum) % MOD

                    # For `dp_diff_one_conflict[c_u][c_p]`:
                    #  1. All previous children were `all_ok`, and `v` is `one_conflict`.
                    #  2. One previous child was `one_conflict`, and `v` is `no_conflict`.
                    next_dp_diff_one_conflict[c_u][c_p] = (prev_all_ok_for_cu_cp * term_v_one_conflict_sum) % MOD
                    next_dp_diff_one_conflict[c_u][c_p] = (next_dp_diff_one_conflict[c_u][c_p] + prev_one_conflict_for_cu_cp * term_v_no_conflict_sum) % MOD
            
            # Update `current` DP states with `next` DP states for the next child
            current_dp_same = next_dp_same
            current_dp_diff_all_ok = next_dp_diff_all_ok
            current_dp_diff_one_conflict = next_dp_diff_one_conflict
        
        return current_dp_same, current_dp_diff_all_ok, current_dp_diff_one_conflict

    # Start DFS from root (vertex 0), with a dummy parent indicated by `k_plus_1_dummy_color`.
    final_dp_same, final_dp_diff_all_ok, final_dp_diff_one_conflict = dfs_recursive(0, -1)

    # Calculate the total number of ways for the root node (vertex 0).
    # For the root, there is no parent `p`, so the `c_p` constraint for `u` does not apply.
    # The condition on `u` is: `u` is `c_u`. For any `C \ne c_u`, `u` can have at most one child `v` of color `C`.
    # This scenario is captured by `dp_diff_all_ok[c_u][k_plus_1_dummy_color]` and `dp_diff_one_conflict[c_u][k_plus_1_dummy_color]`.
    # `dp_same` is also part of the solution when root node has a certain color.
    # `dp_same[c_u]` essentially implies all children could be `c_u`. The root *is* `c_u`. No `c_p` conflict.
    # So `final_dp_same[c_u]` for root means `u` is `c_u`, and all children can be `c_u` or `c_x \ne c_u`. For `c_x \ne c_u`, it still applies.
    # Summing up `final_dp_same[c_u]` over all `c_u` works for cases where the entire tree might be monochromatic.
    # The `final_dp_diff_X[c_u][k_plus_1_dummy_color]` handles cases where root `u` is `c_u`, and its children
    # follow the "at most one non-matching color" rule relative to `u`.

    total_ways = 0
    for c_u in range(k):
        # Case 1: All nodes in the tree are colored with `c_u`. This is implicitly covered by `dp_same[c_u]`.
        # `dp_same[c_u]` accumulates ways where `u` is `c_u` and its children can match `c_u` or be different.
        # This allows `u` and its entire subtree to be `c_u`.
        total_ways = (total_ways + final_dp_same[c_u]) % MOD

        # Case 2: `u` is `c_u`, and its children can have colors `c_x \ne c_u`,
        # but only one child can have any particular `c_x`. This is exactly what
        # `final_dp_diff_all_ok[c_u][k_plus_1_dummy_color]` and `final_dp_diff_one_conflict[c_u][k_plus_1_dummy_color]` cover.
        total_ways = (total_ways + final_dp_diff_all_ok[c_u][k_plus_1_dummy_color]) % MOD
        total_ways = (total_ways + final_dp_diff_one_conflict[c_u][k_plus_1_dummy_color]) % MOD
        
    return total_ways

```