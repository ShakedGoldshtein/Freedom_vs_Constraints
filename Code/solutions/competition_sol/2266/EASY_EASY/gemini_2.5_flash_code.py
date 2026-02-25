```python
def solve(N, M, LR_pairs):
    # Segment tree implementation for efficient chair management.
    # Tree nodes store the number of available chairs in their respective ranges.
    # The tree is 1-indexed for chair coordinates [1, M].
    # A size of 4*M + 4 is a safe upper bound for the segment tree array.
    tree = [0] * (4 * M + 4)

    # Helper function to build the segment tree.
    # Initializes all chairs from 'start' to 'end' as available.
    def _build(node, start, end):
        if start == end:
            tree[node] = 1  # Chair 'start' is available
        else:
            mid = (start + end) // 2
            _build(2 * node, start, mid)  # Build left child
            _build(2 * node + 1, mid + 1, end)  # Build right child
            tree[node] = tree[2 * node] + tree[2 * node + 1] # Sum of children's available chairs

    # Helper function to update the segment tree.
    # 'idx' is the chair coordinate to update, 'delta' is the change (+1 for making available, -1 for taking).
    def _update(node, start, end, idx, delta):
        if start == end:
            tree[node] += delta
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            _update(2 * node, start, mid, idx, delta)
        else:
            _update(2 * node + 1, mid + 1, end, idx, delta)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    # Finds the largest available chair 'c' such that query_start <= c <= query_end.
    # Prioritizes searching the right child to find the largest value first.
    def _find_rightmost_in_range(node, start, end, query_start, query_end):
        # If current node's range is completely outside query range or no chairs available in this segment.
        if query_end < start or query_start > end or tree[node] == 0:
            return -1
        
        # If current node is a leaf, it represents a single chair.
        # If it's available and within the query range, return it.
        if start == end:
            return start
        
        mid = (start + end) // 2
        
        # Check right child first (for larger coordinates)
        res_right = _find_rightmost_in_range(2 * node + 1, mid + 1, end, query_start, query_end)
        if res_right != -1:
            return res_right
        
        # If not found in the right child, check the left child.
        res_left = _find_rightmost_in_range(2 * node, start, mid, query_start, query_end)
        if res_left != -1:
            return res_left
            
        return -1

    # Finds the smallest available chair 'c' such that query_start <= c <= query_end.
    # Prioritizes searching the left child to find the smallest value first.
    def _find_leftmost_in_range(node, start, end, query_start, query_end):
        # If current node's range is completely outside query range or no chairs available in this segment.
        if query_end < start or query_start > end or tree[node] == 0:
            return -1
        
        # If current node is a leaf.
        if start == end:
            return start
        
        mid = (start + end) // 2
        
        # Check left child first (for smaller coordinates)
        res_left = _find_leftmost_in_range(2 * node, start, mid, query_start, query_end)
        if res_left != -1:
            return res_left
        
        # If not found in the left child, check the right child.
        res_right = _find_leftmost_in_range(2 * node + 1, mid + 1, end, query_start, query_end)
        if res_right != -1:
            return res_right
            
        return -1

    # Build the segment tree for chairs 1 to M.
    # If M is 0, no chairs exist, so skip building the tree.
    if M > 0:
        _build(1, 1, M)

    # Sort people:
    # Primary sort key: R_i (right preference boundary) in ascending order.
    # Secondary sort key: L_i (left preference boundary) in ascending order.
    # This greedy order prioritizes people whose 'right side' options are more restricted (smaller R_i).
    # Among those with the same R_i, it prioritizes people whose 'left side' options are also more restricted (smaller L_i).
    people = sorted(LR_pairs, key=lambda x: (x[1], x[0]))

    additional_chairs = 0

    for L, R in people:
        assigned_chair = -1

        # 1. Try to assign to a chair c <= L (left preference)
        # Search for the largest available chair within the valid range [1, L].
        # Clamp L to M to ensure valid chair coordinates.
        query_L_start = 1
        query_L_end = min(L, M)
        
        if query_L_start <= query_L_end: # Check if the query range is valid
            assigned_chair = _find_rightmost_in_range(1, 1, M, query_L_start, query_L_end)
            
        if assigned_chair != -1:
            _update(1, 1, M, assigned_chair, -1) # Mark chair as taken
        else:
            # 2. If left preference not satisfied, try to assign to a chair c >= R (right preference)
            # Search for the smallest available chair within the valid range [R, M].
            # Clamp R to 1 to ensure valid chair coordinates.
            query_R_start = max(1, R)
            query_R_end = M
            
            if query_R_start <= query_R_end: # Check if the query range is valid
                assigned_chair = _find_leftmost_in_range(1, 1, M, query_R_start, query_R_end)
            
            if assigned_chair != -1:
                _update(1, 1, M, assigned_chair, -1) # Mark chair as taken
            else:
                # 3. If neither preference can be satisfied with existing chairs,
                # this person requires an additional chair.
                additional_chairs += 1

    return additional_chairs
```