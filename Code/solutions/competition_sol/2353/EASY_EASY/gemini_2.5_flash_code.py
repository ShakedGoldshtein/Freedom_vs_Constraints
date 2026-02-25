```python
def solve(n, a):
    # CRITICAL REQUIREMENT 1, 4: The solution is a function that takes input parameters and returns the output.
    # CRITICAL REQUIREMENT 2, 3: No stdin/stdout or I/O operations are used.

    # If n is 1, there are no non-empty proper subsets of indices.
    # The condition 0 < k < n becomes 0 < k < 1, which is impossible.
    # Thus, the condition is vacuously true, and 'a' itself is a valid permutation 'b'.
    # Our general approach naturally handles this case by mapping a[0] to a[0].
    # if n == 1:
    #     return a

    # Step 1: Pair each element of 'a' with its original index.
    # This is crucial to reconstruct 'b' based on the original positions.
    indexed_a = []
    for i in range(n):
        indexed_a.append((a[i], i))

    # Step 2: Sort these pairs based on the values of 'a_i'.
    # Since 'a' contains distinct integers, the values will be unique after sorting.
    # indexed_a will become [(v_0, idx_0), (v_1, idx_1), ..., (v_{n-1}, idx_{n-1})]
    # where v_0 < v_1 < ... < v_{n-1} are the sorted values from 'a',
    # and idx_j is the original index of v_j in 'a'.
    indexed_a.sort()

    # Step 3: Initialize the result array 'b' with placeholders.
    b = [0] * n

    # Step 4: Construct 'b' using a cyclic shift of the sorted values.
    # For each element (v_j, idx_j) in the sorted_indexed_a:
    #   The value v_j was originally at index idx_j in array 'a'.
    #   We want to place the (j+1)-th smallest value (cyclically) into b[idx_j].
    #   This (j+1)-th smallest value is v_{(j+1)%n}.
    for j in range(n):
        _, original_index = indexed_a[j]  # The original index of v_j
        
        # The value to be placed at original_index is the (j+1)%n-th smallest value
        # in the sorted list of 'a' elements.
        next_value_in_sorted_list = indexed_a[(j + 1) % n][0]
        
        b[original_index] = next_value_in_sorted_list
    
    # According to a known mathematical property (related to cyclic shifts of ordered sequences),
    # this construction guarantees that for any non-empty proper subset of indices S,
    # sum(a[i] for i in S) != sum(b[i] for i in S) when all elements are distinct.
    # Therefore, a solution always exists under the given constraints (n >= 1, distinct a_i).
    # The problem statement's `return -1` case is not reachable with these constraints.
    return b
```