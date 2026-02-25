```python
import collections

# A class to hold preprocessed data for each box, improving readability.
class BoxData:
    """
    Stores information about a single box.
    Attributes:
        box_idx (int): The 0-based index of the box.
        numbers (list[int]): List of integers originally in the box.
        initial_sum (int): The sum of numbers originally in the box.
    """
    def __init__(self, box_idx: int, numbers: list[int], initial_sum: int):
        self.box_idx = box_idx
        self.numbers = numbers
        self.initial_sum = initial_sum

def solve(k: int, box_numbers_list: list[list[int]]) -> str:
    """
    Determines if Ujan can reorder numbers to make all box sums equal,
    and if so, provides one such reordering.

    Args:
        k (int): The number of boxes.
        box_numbers_list (list[list[int]]): A list where each element is a list
                                             of integers in a corresponding box.

    Returns:
        str: "No" if no solution exists, or "Yes" followed by k lines,
             each specifying (picked_value, target_box_index_1_based).
    """

    total_sum_all_boxes = 0
    box_initial_sums = []
    # Maps each unique number to its original box index (0-based) for quick lookups.
    all_numbers_map = {} 
    
    boxes_data = []

    # Preprocessing: Calculate initial sums and create the all_numbers_map
    for i in range(k):
        current_box_numbers = box_numbers_list[i]
        current_sum = sum(current_box_numbers)
        total_sum_all_boxes += current_sum
        box_initial_sums.append(current_sum)
        
        for num in current_box_numbers:
            # All numbers are guaranteed to be distinct, so no collisions here.
            all_numbers_map[num] = i
        
        boxes_data.append(BoxData(i, current_box_numbers, current_sum))

    # Calculate the target sum for each box. If not divisible by k, no solution.
    if total_sum_all_boxes % k != 0:
        return "No"
    
    target_sum = total_sum_all_boxes // k

    # Step 1: Generate all possible "cycles"
    # A cycle is a sequence of selections (pick from box A, results in placing in B; pick from B, results in placing in C; ...; pick from Z, results in placing in A).
    # Each cycle is represented by:
    #   - `cycle_mask`: a bitmask of boxes involved in this cycle.
    #   - `assignments`: a list of (picked_value, original_box_idx, box_idx_where_it_goes) tuples.
    all_cycles = []
    for start_box_idx in range(k):
        for initial_picked_val_from_start_box in boxes_data[start_box_idx].numbers:
            
            current_val = initial_picked_val_from_start_box
            current_box_original_idx = start_box_idx
            
            path_mask = 0
            path_assignments = [] 
            
            # Keeps track of (box_idx -> value_picked) for the current path to detect cycles and invalid paths.
            visited_path_vals = {} 
            
            # Trace a path to find a cycle
            while True:
                # If we've visited this box in the current path trace:
                if (path_mask & (1 << current_box_original_idx)):
                    # Check if it's a valid cycle completion: returned to start_box_idx with start_val.
                    if current_box_original_idx == start_box_idx and current_val == initial_picked_val_from_start_box:
                        all_cycles.append((path_mask, path_assignments))
                    break # Path ends, either valid cycle or invalid loop/revisit

                # Mark current box as visited in this path trace
                path_mask |= (1 << current_box_original_idx)
                visited_path_vals[current_box_original_idx] = current_val

                # Calculate the value that MUST be placed into current_box_original_idx
                # if current_val was picked from it, to achieve target_sum.
                val_to_place_in_current_box = target_sum - (box_initial_sums[current_box_original_idx] - current_val)
                
                # If this required value doesn't exist among any original numbers, this path is invalid.
                if val_to_place_in_current_box not in all_numbers_map:
                    break 
                
                # Find which box the required value originally came from.
                next_original_box_idx = all_numbers_map[val_to_place_in_current_box]

                # Store the assignment for this step of the cycle:
                # (value_picked, from_which_box, to_which_box_it_should_go)
                path_assignments.append((current_val, current_box_original_idx, next_original_box_idx))

                # Move to the next step in the path
                current_val = val_to_place_in_current_box
                current_box_original_idx = next_original_box_idx

    # Step 2: Dynamic Programming to combine disjoint cycles
    # dp[mask]: True if the boxes represented by 'mask' can be perfectly balanced
    #           by combining disjoint cycles.
    # solution_path[mask]: Stores the index of the cycle used to transition
    #                      from a smaller mask to 'mask'. Used for reconstruction.
    
    dp = [False] * (1 << k)
    solution_path = [None] * (1 << k) # Stores index of cycle from all_cycles
    
    dp[0] = True # Base case: An empty set of boxes is balanced (vacuously true)

    # Iterate through all possible masks (subsets of boxes)
    for mask in range(1 << k):
        if not dp[mask]: # Only extend from masks that are reachable (i.e., balanced)
            continue
        
        # Optimization: Find the smallest-indexed box not yet covered by 'mask'.
        # We will try to add a cycle that specifically covers this 'first_uncovered_box_idx'.
        # This helps avoid redundant calculations by enforcing a canonical way to build masks.
        first_uncovered_box_idx = -1
        for i in range(k):
            if not ((mask >> i) & 1): # If box 'i' is NOT in 'mask'
                first_uncovered_box_idx = i
                break
        
        if first_uncovered_box_idx == -1: # All boxes are covered in this 'mask'
            continue # No more boxes to add, this 'mask' is a complete solution (or part of one)
        
        # Iterate through all pre-generated cycles to find one that can extend 'mask'
        for cycle_idx, (cycle_sub_mask, assignments) in enumerate(all_cycles):
            # 1. The current cycle must cover `first_uncovered_box_idx`.
            if not ((cycle_sub_mask >> first_uncovered_box_idx) & 1):
                continue
            
            # 2. The current cycle must NOT overlap with boxes already covered in `mask`.
            if (mask & cycle_sub_mask) != 0:
                continue

            # If both conditions are met, this cycle can extend the current 'mask'
            next_mask = mask | cycle_sub_mask
            if not dp[next_mask]: # If 'next_mask' has not been reached yet
                dp[next_mask] = True
                solution_path[next_mask] = cycle_idx # Store which cycle was used to reach 'next_mask'

    # Step 3: Reconstruct the solution if a path to `(1 << k) - 1` (all boxes covered) exists.
    if dp[(1 << k) - 1]:
        # `final_assignments` will store the (picked_value, target_box_index_1_based)
        # for each of the k boxes, indexed by their original box_idx.
        final_assignments = [None] * k 
        
        current_mask = (1 << k) - 1 # Start from the final mask (all boxes covered)
        while current_mask > 0:
            cycle_idx = solution_path[current_mask]
            cycle_sub_mask, assignments = all_cycles[cycle_idx]
            
            # Add assignments from this cycle to the final solution
            for picked_val, original_box_idx, placed_in_box_idx in assignments:
                final_assignments[original_box_idx] = (picked_val, placed_in_box_idx + 1) # +1 for 1-based indexing in output
            
            # Remove the boxes covered by this cycle from `current_mask`
            current_mask ^= cycle_sub_mask 
        
        # Format the output string
        result_lines = ["Yes"]
        for val, target_box_idx in final_assignments:
            result_lines.append(f"{val} {target_box_idx}")
        
        return "\n".join(result_lines)
    else:
        return "No"

```