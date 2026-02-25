```python
import collections

def calculate_max_column_sums(n: int, w: int, arrays_data: list[list[int]]) -> list[int]:
    """
    Calculates the maximum sum of integers for each column from 1 to w,
    considering n arrays that can slide horizontally within their rows.

    This solution achieves optimal time and space complexity, O(sum(L_i) + W),
    where sum(L_i) is the total length of all arrays and W is the table width.
    It uses a monotonic deque to find the maximum possible value an array can contribute
    to each column, and then accumulates these contributions using a difference array.

    Args:
        n: The number of arrays (rows).
        w: The width of the table (columns).
        arrays_data: A list of lists, where each inner list represents an array.
                     The first element is its length l_i, followed by l_i integers.

    Returns:
        A list of w integers, where the j-th integer is the maximum sum for column j+1.

    Raises:
        ValueError: If n or w are outside their specified constraints.
    """
    if not (1 <= n <= 10**6 and 1 <= w <= 10**6):
        raise ValueError("Constraints on n and w (1 <= n, w <= 10^6) not met.")

    # `diff_array` will accumulate the contributions for each column.
    # `diff_array[j]` stores the value to be added starting from column `j`.
    # `diff_array[j+1]` is used to cancel the effect at `j+1`, making it a point update.
    # It has length `w+1` to safely handle `diff_array[w]` when updating column `w-1`.
    diff_array = [0] * (w + 1)

    # Process each array provided in the input.
    for array_info in arrays_data:
        l_i = array_info[0]
        a_i = array_info[1:]

        # A monotonic deque `dq` is used to find the maximum element in a variable-sized
        # sliding window over `a_i`. `dq` stores indices `k` of `a_i` such that `a_i[k]` values
        # are in decreasing order from front to back. `dq[0]` always holds the index of
        # the maximum element in the current window.
        dq = collections.deque()
        
        # `k_ptr` is the pointer for the right end of the monotonic deque. It ensures
        # that each element of `a_i` is pushed onto the deque at most once across all `j` iterations
        # for this array, contributing to overall O(L_i) complexity for deque operations.
        k_ptr = 0 

        # Iterate through all target columns `j` from `0` to `w-1`.
        for j in range(w):
            # Calculate the effective window boundaries `[k_start_for_j, k_end_for_j]`
            # for indices `k` within `a_i`.
            # `k_end_for_j`: The rightmost index in `a_i` that could align with column `j`
            #                if the array starts at column 0.
            k_end_for_j = min(l_i - 1, j)
            # `k_start_for_j`: The leftmost index in `a_i` that could align with column `j`
            #                 while the array remains entirely within the table bounds.
            #                 `(w - l_i)` is the maximum allowed starting column for `a_i`.
            k_start_for_j = max(0, j - (w - l_i))

            max_element_in_window = 0  # Default contribution if window is invalid or all elements are negative

            # Only proceed if the window is valid (start index <= end index).
            if k_start_for_j <= k_end_for_j:
                # Expand the window to the right: add elements from `k_ptr` up to `k_end_for_j` to the deque.
                while k_ptr <= k_end_for_j:
                    # Remove elements from the back of the deque that are smaller than or equal to
                    # the new element, as they can no longer be the maximum.
                    while dq and a_i[dq[-1]] <= a_i[k_ptr]:
                        dq.pop()
                    dq.append(k_ptr)
                    k_ptr += 1
                
                # Shrink the window from the left: remove elements from the front of the deque
                # whose indices are now outside the current window `[k_start_for_j, k_end_for_j]`.
                while dq and dq[0] < k_start_for_j:
                    dq.popleft()
                
                # The maximum value in the current window `[k_start_for_j, k_end_for_j]` is `a_i[dq[0]]`.
                max_element_in_window = a_i[dq[0]]
            
            # The actual contribution of array `i` to column `j` is `max(0, max_element_in_window)`.
            # If `max_element_in_window` is negative, we consider its contribution as 0 (by excluding it).
            actual_val_for_col_j = max(0, max_element_in_window)

            # Apply this contribution as a point update to the `diff_array`.
            # `diff_array[j]` is incremented by `actual_val_for_col_j`.
            # `diff_array[j+1]` is decremented by `actual_val_for_col_j` to localized the effect to column `j`.
            diff_array[j] += actual_val_for_col_j
            diff_array[j+1] -= actual_val_for_col_j
            
    # After processing all arrays, compute the prefix sums of `diff_array`
    # to get the final `max_sums` for each column.
    final_max_sums = [0] * w
    current_column_sum_accumulator = 0
    for j in range(w):
        current_column_sum_accumulator += diff_array[j]
        final_max_sums[j] = current_column_sum_accumulator

    return final_max_sums

# The problem specifies that the solution should be a function accepting input parameters
# and returning the result. This function acts as the entry point following that format.
def solve_problem_entry(n: int, w: int, arrays_raw_input: list[list[int]]) -> list[int]:
    """
    Entry point for the problem, parsing the raw input into a structured format
    and calling the core logic function.

    Args:
        n: The number of arrays.
        w: The width of the table.
        arrays_raw_input: A list where each inner list represents an array's data.
                          Format: [l_i, a_i1, a_i2, ..., a_il_i].

    Returns:
        A list of w integers, the maximum sum for each column.
    """
    # The `arrays_raw_input` is already in the required format
    # `[l_i, a_i1, ..., a_il_i]`, so it can be passed directly.
    return calculate_max_column_sums(n, w, arrays_raw_input)

```