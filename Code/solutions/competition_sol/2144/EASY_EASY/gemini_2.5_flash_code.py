```python
import collections

def solve(k_val, boxes_data):
    K = k_val
    
    # Store box numbers as sets for O(1) average-case lookup.
    # boxes_data is a list of lists. Each inner list is [n_i, a_i1, ..., a_in_i].
    BOXES_SETS = [set(nums[1:]) for nums in boxes_data]

    # Pre-processing: Calculate initial sums and map values to their original box index.
    total_sum_all_boxes = 0
    box_initial_sums = [0] * K
    val_to_box_idx = {}  # Maps integer value to its 0-indexed original box ID

    for i in range(K):
        current_box_sum = 0
        for val in boxes_data[i][1:]:  # Numbers start from index 1 in the input format
            current_box_sum += val
            val_to_box_idx[val] = i
        box_initial_sums[i] = current_box_sum
        total_sum_all_boxes += current_box_sum

    # Check if a balanced state is possible
    if total_sum_all_boxes % K != 0:
        return "No"

    target_sum_per_box = total_sum_all_boxes // K

    # dp[mask] stores a dictionary:
    # { start_val_of_chain: (last_val_of_chain, picked_vals_set_in_chain, assignments_map_for_chain) }
    #   - start_val_of_chain: The value picked from the "logical start" box of this chain.
    #   - last_val_of_chain: The value picked from the "logical end" box of this chain.
    #   - picked_vals_set_in_chain: A set of all values picked from boxes within this `mask` (for O(1) distinctness check).
    #   - assignments_map_for_chain: {box_idx: val_picked_from_box_idx} for reconstruction.
    dp = [{} for _ in range(1 << K)]

    # Base cases: single-box chains
    for i in range(K):
        for val_i in boxes_data[i][1:]:  # Iterate through numbers in the box
            dp[1 << i][val_i] = (val_i, {val_i}, {i: val_i})

    # Build paths using bitmask DP
    for mask in range(1, 1 << K):
        for i in range(K):  # `i` is the box we are trying to add as the *last* element in a path
            if not (mask & (1 << i)):  # If box 'i' is not in the current mask, skip
                continue
            
            prev_mask = mask ^ (1 << i)  # `mask` without box `i`
            if prev_mask == 0:  # Base cases handled, skip if `mask` is a single bit
                continue
            
            # Iterate through existing paths in `prev_mask`
            for start_val_first in dp[prev_mask]:
                (last_val_prev, prev_picked_vals_set, prev_assignments_map) = dp[prev_mask][start_val_first]

                # We want to pick `val_to_pick_from_i` from box `i`.
                # This `val_to_pick_from_i` must be such that if `last_val_prev` is placed into box `i`,
                # and `val_to_pick_from_i` is picked from box `i`, then box `i` sums to `target_sum_per_box`.
                # S_i - val_to_pick_from_i + last_val_prev = target_sum_per_box
                # => val_to_pick_from_i = S_i - target_sum_per_box + last_val_prev
                val_to_pick_from_i = box_initial_sums[i] - target_sum_per_box + last_val_prev

                # Check if `val_to_pick_from_i` exists in box `i` and hasn't been picked yet in this path
                if val_to_pick_from_i in BOXES_SETS[i]:
                    if val_to_pick_from_i in prev_picked_vals_set:
                        continue # This would mean picking the same number twice, which is invalid

                    # Extend the path
                    new_picked_vals_set = prev_picked_vals_set.union({val_to_pick_from_i})
                    new_assignments_map = prev_assignments_map.copy()
                    new_assignments_map[i] = val_to_pick_from_i
                    
                    # Store the extended path in dp
                    dp[mask][start_val_first] = (val_to_pick_from_i, new_picked_vals_set, new_assignments_map)

    # Collect all valid cycles
    # `final_solutions` will store (mask_of_cycle, assignments_map_for_cycle)
    # `assignments_map_for_cycle`: {box_idx: val_picked_from_box_idx}
    final_solutions = [] 
    for mask in range(1, 1 << K):
        if not dp[mask]:
            continue
        
        for start_val_first in dp[mask]:
            (last_val_last, picked_vals_set, assignments_map_for_cycle) = dp[mask][start_val_first]

            # Find the box from which `start_val_first` was originally picked
            # This identifies the "first" box in the chain (b_0)
            first_box_idx_in_chain = -1
            for box_idx_in_map in assignments_map_for_cycle:
                if assignments_map_for_cycle[box_idx_in_map] == start_val_first:
                    first_box_idx_in_chain = box_idx_in_map
                    break
            
            # Check if this path forms a cycle:
            # If `last_val_last` is placed into the `first_box_idx_in_chain`,
            # and `start_val_first` is picked from `first_box_idx_in_chain`,
            # then `start_val_first = S_{first_box_idx_in_chain} - target_sum_per_box + last_val_last`.
            if start_val_first == (box_initial_sums[first_box_idx_in_chain] - target_sum_per_box + last_val_last):
                final_solutions.append((mask, assignments_map_for_cycle))

    # Second DP: Combine disjoint cycles to cover all K boxes
    # solution_dp[mask_covered] stores a list of `assignments_map_for_cycle` that sum up to `mask_covered`
    solution_dp = [None] * (1 << K)
    solution_dp[0] = [] # Base case: empty mask covered by empty list of assignments maps

    for mask_covered in range(1, 1 << K):
        for current_cycle_mask, picked_vals_map_for_cycle in final_solutions:
            # If `current_cycle_mask` is a submask of `mask_covered`
            if (mask_covered & current_cycle_mask) == current_cycle_mask: 
                remaining_mask = mask_covered ^ current_cycle_mask
                if solution_dp[remaining_mask] is not None:
                    # Found a way to cover `mask_covered` by adding this cycle
                    solution_dp[mask_covered] = solution_dp[remaining_mask] + [picked_vals_map_for_cycle]
                    break # Move to the next `mask_covered`

    # Check if a solution covering all K boxes was found
    if solution_dp[(1 << K) - 1] is not None:
        result_lines = ["Yes"]
        
        # Consolidate all picked values into a single map {original_box_idx: picked_value}
        all_picked_val_map = {}
        for picked_vals_map_for_cycle in solution_dp[(1 << K) - 1]:
             all_picked_val_map.update(picked_vals_map_for_cycle)

        # Reconstruct the final (value_picked, destination_box_index) assignments
        final_assignments_output = []
        for box_idx_from in range(K):
            val_picked_from_box = all_picked_val_map[box_idx_from]
            
            # If `val_picked_from_box` is chosen from `box_idx_from`,
            # then `box_idx_from` needs to receive `val_to_receive_by_box_from`.
            # `val_to_receive_by_box_from = target_sum_per_box - (box_initial_sums[box_idx_from] - val_picked_from_box)`.
            # This `val_to_receive_by_box_from` must have been picked from some box, say `destination_box_idx`.
            # Therefore, `val_picked_from_box` (from `box_idx_from`) is placed into `destination_box_idx`.
            
            val_to_receive_by_box_from = target_sum_per_box - (box_initial_sums[box_idx_from] - val_picked_from_box)
            
            # The box that sent `val_to_receive_by_box_from` (i.e., its original box index) is the destination for `val_picked_from_box`.
            destination_box_idx = val_to_box_idx[val_to_receive_by_box_from]
            
            # Output uses 1-indexed box numbers
            final_assignments_output.append((val_picked_from_box, destination_box_idx + 1))
        
        # The output order is by original box index (1 to K), which is naturally achieved by iterating range(K)
        for val, target_box_idx in final_assignments_output:
            result_lines.append(f"{val} {target_box_idx}")
        
        return "\n".join(result_lines)
    else:
        return "No"

```