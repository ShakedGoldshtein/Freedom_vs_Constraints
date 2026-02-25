```python
def solve_problem(n, a_input_list):
    """
    Solves the Farmer John program problem.

    Args:
        n (int): The upper bound for x, and size of the sequence a.
        a_input_list (list): A list of integers a_2, a_3, ..., a_n.

    Returns:
        list: A list of integers, where the i-th element is the final value of y
              for a_1 = i+1, or -1 if the program does not terminate.
    """
    # Memoization table for results of paths starting at x >= 2.
    # cache[x] stores (cumulative_y_increase, final_x_state)
    # final_x_state: 0 if x <= 0, n+1 if x > n, -1 if a cycle is detected.
    # We use (None, None) to indicate an uncomputed state.
    # A computed result (-1, -1) explicitly marks a cycle.
    cache = [(None, None)] * (n + 2) 

    # Path tracking for cycle detection during the DP precomputation.
    # recursion_stack[x] = True if x is currently in the recursion stack,
    # indicating a cycle if visited again before unwinding.
    recursion_stack = [False] * (n + 2)

    def get_a_val_fixed(idx):
        """
        Retrieves the value of a_idx from the fixed part of the sequence.
        This is for x >= 2, where a_x corresponds to a_input_list[x-2].
        """
        return a_input_list[idx - 2]

    def calculate_path_from_x_ge_2(curr_x):
        """
        Recursively calculates the outcome (total y, final x state)
        for a path starting at curr_x (where curr_x >= 2).
        """
        # Base case: If x is out of bounds, no further y is added, and curr_x is the termination state.
        if curr_x <= 0 or curr_x > n:
            return 0, curr_x  
        
        # If result is already computed, return it directly.
        if cache[curr_x][0] is not None:
            return cache[curr_x]
        
        # If curr_x is in the current recursion stack, a cycle is detected.
        if recursion_stack[curr_x]:
            cache[curr_x] = (-1, -1)  # Mark as non-terminating (cycle)
            return -1, -1

        # Mark curr_x as being in the recursion stack.
        recursion_stack[curr_x] = True

        # Get a_x for the current x
        val_a_x = get_a_val_fixed(curr_x)

        # Step 2: x = curr_x + val_a_x, y = y_curr + val_a_x
        x_after_s2 = curr_x + val_a_x
        y_added_s2 = val_a_x

        # Check for termination after Step 2
        if x_after_s2 <= 0 or x_after_s2 > n:
            cache[curr_x] = (y_added_s2, x_after_s2)
            recursion_stack[curr_x] = False
            return y_added_s2, x_after_s2
        
        # Step 3: x = x_after_s2 - val_a_x_after_s2, y = y_after_s2 + val_a_x_after_s2
        # Since x_after_s2 >= 2 (as a_x are positive, so curr_x + val_a_x >= 2+1=3 if curr_x=2, val_a_x=1),
        # val_a_x_after_s2 will always be from the fixed part of `a`.
        val_a_x_after_s2 = get_a_val_fixed(x_after_s2)
        x_after_s3 = x_after_s2 - val_a_x_after_s2
        y_added_s3_total = y_added_s2 + val_a_x_after_s2

        # Recursively get the result from the next state (x_after_s3)
        res_y, res_x = calculate_path_from_x_ge_2(x_after_s3)

        # Remove curr_x from the recursion stack.
        recursion_stack[curr_x] = False 

        if res_y == -1:  # A cycle was detected further down the path
            cache[curr_x] = (-1, -1)
            return -1, -1
        else:
            # Accumulate y and store the final termination state.
            cache[curr_x] = (y_added_s3_total + res_y, res_x)
            return cache[curr_x]

    # Precompute results for all possible starting positions x from 2 to n.
    # This phase correctly identifies all fixed-sequence cycles and termination points.
    for x_val in range(2, n + 1):
        if cache[x_val][0] is None:  # If the result for x_val is not yet computed
            calculate_path_from_x_ge_2(x_val)

    # Process each query (simulating the program with a_1 = i)
    results = []
    for i in range(1, n):  # a_1 takes values from 1 to n-1
        # For each run, the program starts at x=1, y=0.
        # It executes one pair of steps (Step 2 then Step 3) with a_1 = i.
        
        # Step 2: x_new = 1 + a_1, y_new = 0 + a_1
        # Here a_1 is `i`
        x_after_s2 = 1 + i
        y_after_s2 = i

        # Check for termination immediately after Step 2
        if x_after_s2 <= 0 or x_after_s2 > n:
            results.append(y_after_s2)
            continue
        
        # Determine a_x for the x value after Step 2 (x_after_s2)
        # Since a_i are positive, 1 + i will always be >= 2.
        # Thus, a_x for x_after_s2 will always come from the fixed a_input_list.
        val_a_x_after_s2 = get_a_val_fixed(x_after_s2)

        # Step 3: x_new_new = x_after_s2 - val_a_x_after_s2, y_new_new = y_after_s2 + val_a_x_after_s2
        x_after_s3 = x_after_s2 - val_a_x_after_s2
        y_after_s3 = y_after_s2 + val_a_x_after_s2

        # After these two steps, the program is at state (x_after_s3, y_after_s3).
        # We now check if it terminates or if it transitions to a precomputed path.
        if x_after_s3 <= 0 or x_after_s3 > n:
            results.append(y_after_s3)
        elif x_after_s3 == 1:
            # If x returns to 1 after the first two steps, and a_1 is fixed at `i`,
            # this implies an infinite loop (1 -> x_after_s2 -> 1 -> x_after_s2 -> ...).
            results.append(-1)
        else:  # x_after_s3 >= 2, so we can use the precomputed cache
            res_y_from_cache, res_x_from_cache = cache[x_after_s3]
            if res_y_from_cache == -1:  # The path from x_after_s3 leads to a cycle
                results.append(-1)
            else:
                # Add the y accumulated in the first two steps to the y from the cached path.
                results.append(y_after_s3 + res_y_from_cache)
    
    return results
```