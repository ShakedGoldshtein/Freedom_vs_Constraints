```python
import math

class SegmentTree:
    """
    A Segment Tree designed to efficiently find the first 'unset' (value 0) index in a given range.
    It tracks whether a range contains any unset value.
    'True' in tree[node_idx] means all elements in its corresponding range are 'set' (value 1).
    'False' means it contains at least one 'unset' (value 0).
    """
    def __init__(self, size: int):
        """
        Initializes the segment tree.
        Args:
            size (int): The number of elements in the array (0 to size-1).
        """
        self.size = size
        # We need roughly 4*size for a complete binary tree that handles up to 'size' leaves.
        self.tree = [False] * (4 * size)
        self._build(0, 0, size - 1)

    def _build(self, node_idx: int, node_start: int, node_end: int):
        """
        Recursively builds the segment tree. All leaves are initially 'unset' (False).
        """
        if node_start == node_end:
            # Leaf node, initially unset (False)
            self.tree[node_idx] = False
        else:
            mid = (node_start + node_end) // 2
            self._build(2 * node_idx + 1, node_start, mid)
            self._build(2 * node_idx + 2, mid + 1, node_end)
            # A parent node is 'set' (True) only if BOTH children are 'set'.
            # Otherwise, it's 'unset' (False).
            self.tree[node_idx] = self.tree[2 * node_idx + 1] and self.tree[2 * node_idx + 2]

    def update(self, idx: int, value: int):
        """
        Sets the value at a specific index. Here, 'value' is expected to be 1 (set).
        Args:
            idx (int): The 0-based index to update in the original array.
            value (int): The value to set (1 for 'set', 0 for 'unset').
        """
        self._update(0, 0, self.size - 1, idx, value)

    def _update(self, node_idx: int, node_start: int, node_end: int, idx: int, value: int):
        """
        Internal recursive function to update a value in the segment tree.
        """
        if node_start == node_end:
            # Leaf node. If value is 1, it's 'set' (True), otherwise 'unset' (False).
            self.tree[node_idx] = (value == 1)
        else:
            mid = (node_start + node_end) // 2
            if node_start <= idx <= mid:
                self._update(2 * node_idx + 1, node_start, mid, idx, value)
            else:
                self._update(2 * node_idx + 2, mid + 1, node_end, idx, value)
            # Update parent: True if BOTH children are True
            self.tree[node_idx] = self.tree[2 * node_idx + 1] and self.tree[2 * node_idx + 2]

    def query_first_unset(self, query_start_idx: int) -> int | None:
        """
        Finds the first index >= query_start_idx that is 'unset' (value 0).
        Args:
            query_start_idx (int): The 0-based starting index for the search.
        Returns:
            int: The first unset index, or None if no such index exists.
        """
        return self._query_first_unset(0, 0, self.size - 1, query_start_idx)

    def _query_first_unset(self, node_idx: int, node_start: int, node_end: int, query_start_idx: int) -> int | None:
        """
        Internal recursive function to find the first unset index.
        """
        # If the current node's range is entirely before the query start index,
        # or if all elements in this node's range are already 'set', then no unset element
        # can be found here for the current query.
        if node_end < query_start_idx or self.tree[node_idx]:
            return None

        # If it's a leaf node and it's 'unset' (self.tree[node_idx] is False), return its index.
        if node_start == node_end:
            return node_start

        mid = (node_start + node_end) // 2

        # First, try to find in the left child's range.
        # We only search the left child if its range overlaps with or is entirely after query_start_idx.
        if query_start_idx <= mid:
            res = self._query_first_unset(2 * node_idx + 1, node_start, mid, query_start_idx)
            if res is not None:
                return res
        
        # If not found in the left child (or left child was entirely before query_start_idx),
        # try the right child. The search for the right child begins from `mid + 1`.
        return self._query_first_unset(2 * node_idx + 2, mid + 1, node_end, query_start_idx)


def find_increasing_sequences(n: int, a: list[int]) -> list[list[int]]:
    """
    Finds representation of the given array with one or several increasing sequences
    in accordance with Ivan's algorithm.

    The algorithm repeatedly scans the original array from left to right,
    picking unused numbers that are greater than the last picked number in the current sequence.
    This process continues until all numbers are used.

    Optimal Time Complexity: O(N log N)
        - Each element is marked as used exactly once, resulting in N `update` operations on the segment tree (O(N log N)).
        - The `query_first_unset` operation effectively advances a pointer `current_array_scan_idx`
          through the array. In total, this pointer traverses the array once across all passes,
          making O(N) calls to `query_first_unset` (each O(log N)).
        - Total time: O(N log N).
    Optimal Space Complexity: O(N)
        - `output_sequences` stores all N elements (O(N)).
        - The `SegmentTree` uses O(N) space for its internal array.
        - Total space: O(N).

    Args:
        n (int): The number of elements in Ivan's array.
        a (list[int]): Ivan's array of distinct integers.

    Returns:
        list[list[int]]: A list of increasing sequences. Each sequence is a list of integers.
                         Returns an empty list if n is 0 or a is empty.
    """
    if n == 0 or not a:
        return []

    output_sequences: list[list[int]] = []
    
    # Segment tree to track used elements. A value of 1 means 'used', 0 means 'unused'.
    # Initially all elements are unused (0).
    # The segment tree is built to efficiently find the first '0' (unused index).
    used_status_tree = SegmentTree(n)

    total_elements_used = 0

    # Continue generating sequences until all elements from the input array 'a' are used.
    while total_elements_used < n:
        current_sequence: list[int] = []
        last_val_in_sequence = -math.inf  # Use negative infinity for the first comparison in a sequence
        elements_added_this_pass = 0
        
        # This variable tracks the current position in the original array 'a'
        # from where we continue searching for the next unused element.
        current_array_scan_idx = 0 

        # Iterate through the array (conceptually) from left to right,
        # picking elements for the current sequence.
        while True:
            # Efficiently find the next unused index starting from `current_array_scan_idx`.
            # The SegmentTree helps to skip over already used elements in O(log N) time.
            next_unused_idx = used_status_tree.query_first_unset(current_array_scan_idx)
            
            if next_unused_idx is None:
                # No more unused elements in the array from current_array_scan_idx onwards.
                # End of current pass.
                break
            
            value_at_idx = a[next_unused_idx]

            # Ivan's condition: "if current number is the first unused number on this iteration
            # or this number is greater than previous unused number on current iteration"
            # The `-math.inf` handles the "first unused number" part.
            if value_at_idx > last_val_in_sequence:
                current_sequence.append(value_at_idx)
                last_val_in_sequence = value_at_idx
                
                # Mark this element as used in the segment tree.
                used_status_tree.update(next_unused_idx, 1) # 1 means used
                
                elements_added_this_pass += 1
            
            # Important: Continue scanning from the next position, regardless if the element was picked or skipped.
            # This ensures we always move forward in the original array's conceptual scan.
            current_array_scan_idx = next_unused_idx + 1
        
        # If this pass didn't add any elements, but there are still unused elements overall,
        # it indicates an unexpected state. With distinct positive integers and -math.inf as initial
        # `last_val_in_sequence`, a sequence can always be started if elements remain.
        # This break acts as a safeguard against potential infinite loops in unforeseen edge cases,
        # though it should ideally not be reached under the problem's constraints.
        if elements_added_this_pass == 0:
            break

        output_sequences.append(current_sequence)
        total_elements_used += elements_added_this_pass
    
    return output_sequences
```