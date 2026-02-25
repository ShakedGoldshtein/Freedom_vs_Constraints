```python
import bisect
from collections import defaultdict

def solve(N, Q, initial_a_values, queries):
    """
    Solves the mountain travel problem with updates and queries.

    Args:
        N (int): The number of mountains.
        Q (int): The number of queries.
        initial_a_values (list): A list of N integers representing initial mountain heights.
        queries (list): A list of queries, where each query is a list:
                        - Type 0: [0, A, B] for updating a[A] to B.
                        - Type 1: [1, A] for finding the next suitable mountain.

    Returns:
        list: A list of integers, where each integer is the result for a Type 1 query.
              -1 if no such mountain is found.
    """

    # 'a' stores the current heights of the mountains. It is modified by Type 0 queries.
    a = list(initial_a_values)

    # 'indices_of_value' maps each height value to a sorted list of indices where it appears.
    # Example: indices_of_value[5] = [2, 4, 9] means a[2]=5, a[4]=5, a[9]=5.
    # This is used to quickly determine the first occurrence of a height.
    # Operations (add, remove) on these lists can be O(N) in the worst case (if a value appears many times).
    indices_of_value = defaultdict(list)

    # 'first_occurrence_idx' maps each height value to its smallest index in 'a'.
    # This is effectively indices_of_value[val][0].
    # We maintain this separately for O(1) lookup during Type 1 queries.
    first_occurrence_idx = {} # Value -> first index. `N` if not present.

    # --- Initial population of indices_of_value and first_occurrence_idx ---
    for i, val in enumerate(a):
        bisect.insort_left(indices_of_value[val], i) # Add index 'i' to the sorted list for 'val'
    
    # Populate first_occurrence_idx using the initial state of indices_of_value
    for val in indices_of_value:
        first_occurrence_idx[val] = indices_of_value[val][0]

    # --- Helper function to update first_occurrence_idx for a specific value ---
    # This is called when an index that *was* the first occurrence is removed,
    # or when a value's list of indices becomes empty.
    def _update_first_occurrence_for_value(val):
        if val in indices_of_value and indices_of_value[val]:
            first_occurrence_idx[val] = indices_of_value[val][0]
        else:
            first_occurrence_idx.pop(val, None) # Remove entry if no occurrences left

    # --- Process queries ---
    results = [] # Stores results for Type 1 queries

    for query_type, *args in queries:
        if query_type == 0:  # Type 0 query: Update a[idx] to new_val
            idx, new_val = args[0], args[1]
            old_val = a[idx]

            # 1. Update indices_of_value for the old_val: remove 'idx'
            # Use bisect_left to find the index of 'idx' in the sorted list.
            # list.pop() then removes it. This is O(len(list)) in worst case.
            idx_in_list = bisect.bisect_left(indices_of_value[old_val], idx)
            if idx_in_list < len(indices_of_value[old_val]) and indices_of_value[old_val][idx_in_list] == idx:
                indices_of_value[old_val].pop(idx_in_list)
            
            # 2. Update first_occurrence_idx for old_val if 'idx' was its first occurrence
            if old_val in first_occurrence_idx and first_occurrence_idx[old_val] == idx:
                _update_first_occurrence_for_value(old_val)
            
            # 3. Update the mountain height array 'a'
            a[idx] = new_val

            # 4. Update indices_of_value for the new_val: add 'idx'
            # bisect.insort_left keeps the list sorted. This is O(len(list)) in worst case.
            bisect.insort_left(indices_of_value[new_val], idx)
            
            # 5. Update first_occurrence_idx for new_val if 'idx' is a new earliest occurrence
            if new_val not in first_occurrence_idx or idx < first_occurrence_idx[new_val]:
                first_occurrence_idx[new_val] = idx

        elif query_type == 1:  # Type 1 query: Find next suitable mountain
            query_idx = args[0]
            target_height = a[query_idx] # The height of the mountain Chef is currently on
            
            found_result = -1 # Default to -1 if no suitable mountain is found
            
            # Iterate through mountains from 'query_idx + 1' to 'N-1' (rightwards)
            # The first one that satisfies conditions is the "nearest".
            for k in range(query_idx + 1, N):
                current_height = a[k]
                
                # Condition 1: The peak's height must be greater than Chef's current mountain's height.
                if current_height <= target_height:
                    continue
                
                # Condition 2: "there should be no other peak of same height a_j till a_i"
                # This is interpreted as: the height 'current_height' must NOT have appeared
                # in the subarray a[0...query_idx].
                # We check this by seeing if the first global occurrence of 'current_height'
                # is at an index greater than 'query_idx'.
                # `first_occurrence_idx.get(current_height, N)` returns N if current_height
                # is not present in the array, which correctly makes N > query_idx.
                if first_occurrence_idx.get(current_height, N) <= query_idx:
                    continue # current_height appeared in a[0...query_idx], so it's disqualified
                
                # Both conditions met. This is the first (nearest) such mountain found.
                found_result = current_height
                break # Stop searching as we found the nearest one
            
            results.append(found_result)
    
    return results

```