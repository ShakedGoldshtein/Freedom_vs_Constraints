```python
def solve_farmer_john_program(n: int, a_values: list[int]) -> list[int]:
    """
    Simulates Farmer John's program for different starting a_1 values.

    The program operates on two integer variables, x and y, and a sequence a_1, ..., a_n.
    Initially, x = 1 and y = 0.
    The program repeatedly performs two steps:
    1. x = x + a_x, y = y + a_x
    2. x = x - a_x_new, y = y + a_x_new (where a_x_new is evaluated at the new x from step 1)
    The program terminates immediately if, after any step, x <= 0 or x > n.
    If the program runs indefinitely, y is -1.

    Args:
        n: The upper bound for x, and the length of the full sequence a.
        a_values: A list of n-1 integers representing a_2, a_3, ..., a_n.
                  (In a 0-indexed array, a_values[k] corresponds to a_{k+2} from the problem statement.)

    Returns:
        A list of n-1 integers. The i-th element (0-indexed) is the final y value
        when a_1 is set to i+1, or -1 if the program does not terminate.
    """
    # dp_results[x_val] stores a tuple (total_y_increment, final_x_position)
    # for a program starting with initial x = x_val, current y = 0,
    # and using the fixed part of the array A (i.e., A[1:]).
    # This means dp_results is only valid for x_val >= 2, as A[0] (which is a_1) is variable.
    # We initialize with (None, None) to indicate that the state has not been computed.
    #
    # The 'final_x_position' can indicate:
    #   - An actual x value (<=0 or >n) if the program terminates out of bounds.
    #   - -1 if an infinite loop is detected.
    #   - 1 if the program path leads to x=1, requiring a_1 for further steps.
    dp_results = [(None, None)] * (n + 1)
    
    # Precompute results for starting x values from n down to 2.
    # This order allows memoization to be effective for paths that jump to larger x values.
    for start_x in range(n, 1, -1):
        current_x = start_x
        current_y_accum = 0  # Accumulates y change along the current path from start_x
        
        # path_map: Maps x to current_y_accum when x was first visited in this specific path.
        # Used for detecting cycles *within the current computation of dp_results[start_x]*.
        path_map = {} 
        # path_trace: Stores (x, y_accum) tuples for all visited states in the current path.
        # Used to backtrack and update dp_results for all states in this path once the outcome is known.
        path_trace = [] 
        
        while True:
            # Check for immediate termination due to x being out of bounds
            if current_x <= 0 or current_x > n:
                final_y = current_y_accum
                final_x = current_x
                # Update all states in the path_trace with this outcome
                for prev_x, prev_y_at_x in reversed(path_trace):
                    dp_results[prev_x] = (final_y - prev_y_at_x, final_x)
                dp_results[start_x] = (final_y, final_x)
                break
            
            # Check if the current path leads to x=1.
            # If so, this path segment cannot be fully resolved without knowing a_1.
            # We mark it as reaching x=1 and store the accumulated y change.
            if current_x == 1:
                final_y = current_y_accum
                final_x = 1  # Special indicator for "path reached x=1"
                for prev_x, prev_y_at_x in reversed(path_trace):
                    dp_results[prev_x] = (final_y - prev_y_at_x, final_x)
                dp_results[start_x] = (final_y, final_x)
                break

            # Check for a cycle within the current path (prioritize over memoization hit)
            if current_x in path_map:
                # Cycle detected. Mark all states in path_trace and start_x as leading to an infinite loop.
                for prev_x, _ in reversed(path_trace):
                    dp_results[prev_x] = (-1, -1)
                dp_results[start_x] = (-1, -1)
                break
            
            # Check if the current state's outcome has already been computed (memoization hit)
            if dp_results[current_x][0] is not None:
                prev_res_y, prev_res_x = dp_results[current_x]
                
                if prev_res_x == -1:  # The encountered state leads to a cycle
                    final_y = -1
                    final_x = -1
                elif prev_res_x == 1: # The encountered state leads to x=1
                    final_y = current_y_accum + prev_res_y
                    final_x = 1
                else:                 # The encountered state leads to termination
                    final_y = current_y_accum + prev_res_y
                    final_x = prev_res_x
                
                # Update all states in the current path_trace with the determined outcome
                for prev_x, prev_y_at_x in reversed(path_trace):
                    if final_x == -1: # Propagate cycle
                        dp_results[prev_x] = (-1, -1)
                    else:             # Propagate termination or reach x=1
                        dp_results[prev_x] = (final_y - prev_y_at_x, final_x)
                
                dp_results[start_x] = (final_y, final_x)
                break

            # If not terminated, not a cycle, not x=1, and not in cache, add to path and compute next step
            path_map[current_x] = current_y_accum
            path_trace.append((current_x, current_y_accum))

            # a_values is 0-indexed for a_2 ... a_n.
            # So a_{current_x} (for current_x >= 2) maps to a_values[current_x - 2].
            val1 = a_values[current_x - 2] 

            # Step 2: x = x + val1, y = y + val1
            x_after_step2 = current_x + val1
            y_after_step2 = current_y_accum + val1
            
            # Check termination after step 2
            if x_after_step2 <= 0 or x_after_step2 > n:
                final_y = y_after_step2
                final_x = x_after_step2
                for prev_x, prev_y_at_x in reversed(path_trace):
                    dp_results[prev_x] = (final_y - prev_y_at_x, final_x)
                dp_results[start_x] = (final_y, final_x)
                break
            
            # Since current_x >= 2 and val1 >= 1, x_after_step2 will always be >= 3.
            # Thus, val2 will also refer to an element in a_values (a_2, ..., a_n).
            val2 = a_values[x_after_step2 - 2] 
            
            # Step 3: x = x - val2, y = y + val2
            current_x = x_after_step2 - val2
            current_y_accum = y_after_step2 + val2

    # Now calculate results for each possible initial a_1 value (from 1 to n-1)
    results = []
    for i in range(1, n):  # a_1 takes values 1, 2, ..., n-1
        current_x = 1
        current_y = 0  # Initial y for this specific run
        
        # Simulate the first pair of operations (Step 2 and 3)
        # using the current 'i' as a_1.
        
        val1 = i  # a_1 is set to 'i'
        
        # Step 2: x = x + val1, y = y + val1
        x_step2 = current_x + val1
        y_step2 = current_y + val1

        # Check termination after step 2
        if x_step2 <= 0 or x_step2 > n:
            results.append(y_step2)
            continue
        
        # Determine val2 for step 3.
        # If x_step2 is 1, a_1 ('i') is used again.
        # Otherwise (x_step2 >= 2), a_values (a_2, ..., a_n) are used.
        val2 = i if x_step2 == 1 else a_values[x_step2 - 2]
        
        # Step 3: x = x - val2, y = y + val2
        x_step3 = x_step2 - val2
        y_step3 = y_step2 + val2
        
        # Check termination after step 3
        if x_step3 <= 0 or x_step3 > n:
            results.append(y_step3)
            continue

        # If x_step3 is 1: This means x returned to 1 after the first full iteration.
        # Since a_1 (which is 'i') is always positive, and x=1 will then use a_1 again,
        # this path forms an infinite loop (1 -> (1+i) -> 1 -> ...).
        if x_step3 == 1:
            results.append(-1)
            continue
        
        # Otherwise, x_step3 is >= 2. We can now use the precomputed dp_results.
        # dp_results[x_step3] stores (total_y_added_from_x_step3, final_x_after_x_step3_path).
        dp_y, dp_final_x = dp_results[x_step3]
        
        if dp_final_x == -1:  # Propagates a cycle from the fixed part
            results.append(-1)
        elif dp_final_x == 1: # The path from x_step3 leads to x=1.
            # If the path starting from x_step3 leads back to x=1, it means the
            # entire program (starting at x=1, using a_1=i) forms an infinite loop.
            # (e.g., 1 -> x_step3 --(dp_results)--> 1).
            results.append(-1)
        else:                 # Program terminates (dp_final_x is out of bounds)
            results.append(y_step3 + dp_y)
            
    return results

```