```python
def max_column_sums(n, w, arrays):
    """
    Calculate the maximum sum for each column when arrays can be optimally placed in rows.

    Args:
        n: Number of arrays (rows).
        w: Number of columns (width of the table).
        arrays: List of tuples, where each tuple is (length, [elements]) for the i-th array.

    Returns:
        List of maximum sums for each column (1-based to w).
    """
    # Preprocess each array: for each possible column position, compute prefix sums
    # and track the maximum sum achievable when the array is placed in that column.
    column_max_sums = [0] * (w + 2)  # 1-based indexing for columns

    for length, elements in arrays:
        if length == 0:
            continue

        # Compute prefix sums for the current array
        prefix = [0] * (length + 1)
        for i in range(1, length + 1):
            prefix[i] = prefix[i - 1] + elements[i - 1]

        # For each possible starting column (1-based), compute the sum it contributes
        # to each column it covers, and update the column_max_sums accordingly.
        max_start = w - length + 1
        for start_col in range(1, max_start + 1):
            end_col = start_col + length - 1
            total = prefix[length]  # Total sum of the array

            # The array contributes to columns start_col to end_col.
            # We need to find the best segment of the array to align with these columns.
            # The optimal is to take the entire array (since all elements are included),
            # but we can also consider partial sums if the array is longer than the window.
            # However, since the array must be placed entirely within the table,
            # the entire array is always used, and its sum is added to the columns it covers.

            # Update the column sums for the covered columns
            for col in range(start_col, end_col + 1):
                if col <= w:
                    column_max_sums[col] += elements[col - start_col]

    # Now, for each column, we need to find the maximum sum achievable by selecting
    # a subset of arrays (rows) such that their placements cover the column.
    # This is equivalent to, for each column, finding the maximum sum of elements
    # from arrays that can be placed to cover this column.

    # Reset the column sums to compute the maximum per column
    max_sums = [0] * (w + 1)  # 1-based

    # For each array, determine the best placement to maximize each column's sum
    for length, elements in arrays:
        if length == 0:
            continue

        prefix = [0] * (length + 1)
        for i in range(1, length + 1):
            prefix[i] = prefix[i - 1] + elements[i - 1]

        # For each possible column, determine if this array can contribute to it
        # and if so, what's the maximum contribution.
        # The array can contribute to columns j where it can be placed such that j is covered.
        # i.e., start_col <= j <= start_col + length - 1
        # => start_col in [max(1, j - length + 1), min(w - length + 1, j)]

        # Precompute for each column j, the maximum sum achievable by placing this array
        # such that it covers column j.
        # The maximum is achieved by placing the array to start at start_col = max(1, j - length + 1),
        # because this maximizes the overlap with column j (the array is as far left as possible).
        # Then, the element of the array that aligns with column j is at position (j - start_col).
        # The sum contributed to column j is elements[j - start_col].

        # So for each column j, the contribution from this array is:
        # elements[j - start_col], where start_col = max(1, j - length + 1)
        # But we must ensure that start_col + length - 1 <= w, i.e., start_col <= w - length + 1
        # So start_col is in [max(1, j - length + 1), min(w - length + 1, j)]

        # However, since the array must be entirely within the table, the start_col must satisfy:
        # 1 <= start_col <= w - length + 1
        # And for the array to cover column j: start_col <= j