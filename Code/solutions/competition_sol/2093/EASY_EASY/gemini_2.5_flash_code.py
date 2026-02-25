```python
import math

class SegmentTree:
    def __init__(self, n, arr):
        self.n = n
        # Stores (value, original_index) tuples.
        # Initializing with (infinity, -1) to represent unused/empty slots.
        self.tree = [(math.inf, -1)] * (4 * n) 
        self.arr_ref = arr # Reference to the original array values for retrieval
        self._build(1, 0, n - 1)

    def _build(self, v, tl, tr):
        """Builds the segment tree recursively."""
        if tl == tr:
            self.tree[v] = (self.arr_ref[tl], tl)
        else:
            tm = (tl + tr) // 2
            self._build(2 * v, tl, tm)
            self._build(2 * v + 1, tm + 1, tr)
            # A node stores the minimum value in its range.
            # If values are equal, the one with the smaller index is considered minimum.
            self.tree[v] = min(self.tree[2 * v], self.tree[2 * v + 1])

    def update(self, v, tl, tr, pos, new_val):
        """Updates the value at a specific position in the segment tree."""
        if tl == tr:
            self.tree[v] = (new_val, pos)
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(2 * v, tl, tm, pos, new_val)
            else:
                self.update(2 * v + 1, tm + 1, tr, pos, new_val)
            self.tree[v] = min(self.tree[2 * v], self.tree[2 * v + 1])

    def query_first_greater(self, v, tl, tr, query_start_idx, threshold):
        """
        Finds the smallest index `i` such that `i >= query_start_idx` and `a[i]` (its current value in the tree) > `threshold`.
        """
        # If the current segment's range is entirely before query_start_idx,
        # or if all elements in this segment are already 'used' (math.inf),
        # then no candidate can be found in this segment.
        if tr < query_start_idx or self.tree[v][0] == math.inf:
            return None

        # If it's a leaf node
        if tl == tr:
            if self.tree[v][0] > threshold:
                return self.tree[v][1] # Return the index
            else:
                return None # Value at this leaf is not greater than threshold

        tm = (tl + tr) // 2
        
        # Search in the left child first to find the smallest possible index.
        # Only search left if its range overlaps with or is after query_start_idx.
        if tm >= query_start_idx:
            res_left = self.query_first_greater(2 * v, tl, tm, query_start_idx, threshold)
            if res_left is not None:
                return res_left
        
        # If not found in the left child (or left child was skipped), search in the right child.
        res_right = self.query_first_greater(2 * v + 1, tm + 1, tr, query_start_idx, threshold)
        return res_right

def solve(n: int, a: list[int]) -> list[list[int]]:
    sequences = []
    
    # Initialize segment tree. It stores the values of array 'a' and their original indices.
    # When an element is used, its value in the segment tree is updated to math.inf.
    st = SegmentTree(n, a)
    
    num_used_elements = 0
    # Continue as long as there are unused elements in the original array
    while num_used_elements < n:
        current_sequence = []
        # According to constraints, a_i >= 1. Use 0 as initial 'last_val' to allow first element to be chosen.
        last_val_in_seq = 0 
        # The search for the next element in the current sequence starts from this index.
        # It ensures we iterate from left to right as per the algorithm.
        current_search_idx = 0 
        
        # Build the current increasing sequence
        while True:
            # Query the segment tree for the smallest index `i` (>= current_search_idx)
            # where the value `a[i]` is greater than `last_val_in_seq`.
            found_idx = st.query_first_greater(1, 0, n - 1, current_search_idx, last_val_in_seq)
            
            if found_idx is None:
                # No more elements can be added to the current sequence
                break 
            
            # Retrieve the original value using the found index
            original_val = a[found_idx]
            current_sequence.append(original_val)
            last_val_in_seq = original_val
            
            # Mark this element as used by setting its value in the segment tree to infinity.
            st.update(1, 0, n - 1, found_idx, math.inf)
            num_used_elements += 1
            
            # For the next element in the current sequence, start searching from the index
            # immediately after the one just picked.
            current_search_idx = found_idx + 1
        
        # After completing a sequence, add it to the list of all sequences.
        # This condition should always be true if num_used_elements < n,
        # as the first available element will always start a sequence.
        if current_sequence:
            sequences.append(current_sequence)
        else:
            # Should not happen if loop condition (num_used_elements < n) is true,
            # but serves as a safety break in case of unexpected state.
            break 
            
    return sequences
```