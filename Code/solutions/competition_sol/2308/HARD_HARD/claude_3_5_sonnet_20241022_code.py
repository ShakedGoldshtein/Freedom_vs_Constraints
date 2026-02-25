```python
def solve(n, w, arrays):
    """
    Find max column sums by optimally sliding arrays in rows.
    
    Args:
        n: Number of arrays
        w: Width of table
        arrays: List of arrays where each array is (length, [elements])
    
    Returns:
        List of max sums for each column
    """
    def get_max_at_col(arrays, col, w):
        best = 0
        for i, (length, arr) in enumerate(arrays):
            if length > w:
                continue
                
            # Try each possible position for this array
            max_start = w - length
            curr_best = 0
            for start in range(max_start + 1):
                end = start + length - 1
                if start <= col <= end:
                    pos = col - start
                    curr_best = max(curr_best, arr[pos])
            best += curr_best
            
        return best
    
    # Process arrays into tuples of (length, array)
    processed = []
    for arr in arrays:
        length = arr[0]
        elements = arr[1:]
        processed.append((length, elements))
        
    # Calculate max sum for each column
    result = []
    for col in range(w):
        max_sum = get_max_at_col(processed, col, w)
        result.append(max_sum)
        
    return result
```