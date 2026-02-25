```python
def solve(N, bags):
    # Normalize bags such that x_i <= y_i for each pair, then sort by the smaller value.
    # This prepares the data for a sweep-line approach.
    data = sorted([(min(x, y), max(x, y)) for x, y in bags])

    # Precompute prefix minimums/maximums for the 'left' part of a partition.
    # If a bag (l_j, r_j) is in the left part (j < k), l_j is assigned to blue, r_j to red.
    min_r_pref = [float('inf')] * N
    max_r_pref = [float('-inf')] * N
    min_l_pref = [float('inf')] * N
    max_l_pref = [float('-inf')] * N

    curr_min_r = float('inf')
    curr_max_r = float('-inf')
    curr_min_l = float('inf')
    curr_max_l = float('-inf')

    for i in range(N):
        l_i, r_i = data[i]
        curr_min_r = min(curr_min_r, r_i)
        curr_max_r = max(curr_max_r, r_i)
        curr_min_l = min(curr_min_l, l_i)
        curr_max_l = max(curr_max_l, l_i)
        
        min_r_pref[i] = curr_min_r
        max_r_pref[i] = curr_max_r
        min_l_pref[i] = curr_min_l
        max_l_pref[i] = curr_max_l

    # Precompute suffix minimums/maximums for the 'right' part of a partition.
    # If a bag (l_j, r_j) is in the right part (j >= k), l_j is assigned to red, r_j to blue.
    min_l_suff = [float('inf')] * (N + 1)
    max_l_suff = [float('-inf')] * (N + 1)
    min_r_suff = [float('inf')] * (N + 1)
    max_r_suff = [float('-inf')] * (N + 1)

    for i in range(N - 1, -1, -1):
        l_i, r_i = data[i]
        min_l_suff[i] = min(l_i, min_l_suff[i+1])
        max_l_suff[i] = max(l_i, max_l_suff[i+1])
        min_r_suff[i] = min(r_i, min_r_suff[i+1])
        max_r_suff[i] = max(r_i, max_r_suff[i+1])

    # Initialize the minimum product found so far to a very large value.
    overall_min_product = float('inf')

    # Iterate through all possible split points 'k'.
    # 'k' defines the partition:
    # - Bags data[0] to data[k-1] (left part) have their min value (l_j) blue and max value (r_j) red.
    # - Bags data[k] to data[N-1] (right part) have their min value (l_j) red and max value (r_j) blue.
    for k in range(N + 1):
        current_R_min = float('inf')
        current_R_max = float('-inf')
        current_B_min = float('inf')
        current_B_max = float('-inf')

        # Aggregate values from the left part (bags 0 to k-1)
        if k > 0:
            current_R_min = min(current_R_min, min_r_pref[k-1])
            current_R_max = max(current_R_max, max_r_pref[k-1])
            current_B_min = min(current_B_min, min_l_pref[k-1])
            current_B_max = max(current_B_max, max_l_pref[k-1])
        
        # Aggregate values from the right part (bags k to N-1)
        if k < N:
            current_R_min = min(current_R_min, min_l_suff[k])
            current_R_max = max(current_R_max, max_l_suff[k])
            current_B_min = min(current_B_min, min_r_suff[k])
            current_B_max = max(current_B_max, max_r_suff[k])

        # If both red and blue sets have at least one ball assigned, calculate the product.
        # This check is necessary to avoid (inf - inf) or similar issues for empty sets.
        if current_R_min != float('inf') and current_B_min != float('inf'):
            product = (current_R_max - current_R_min) * (current_B_max - current_B_min)
            overall_min_product = min(overall_min_product, product)

    return overall_min_product
```