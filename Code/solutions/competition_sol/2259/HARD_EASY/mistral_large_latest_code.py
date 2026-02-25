```python
def solve(n, q, arr, queries):
    # Preprocess the array to mark valid elements and their positions
    valid = []
    for idx in range(n):
        if arr[idx] == idx + 1:
            valid.append(idx)

    # Precompute prefix and suffix counts for efficient range queries
    prefix = [0] * (n + 2)
    for i in range(len(valid)):
        prefix[i + 1] = prefix[i] + 1

    suffix = [0] * (n + 2)
    for i in range(len(valid) - 1, -1, -1):
        suffix[i] = suffix[i + 1] + 1

    # Process each query
    results = []
    for x, y in queries:
        left = x
        right = n - 1 - y

        if left > right:
            results.append(0)
            continue

        # Find the first valid element >= left
        low, high = 0, len(valid)
        while low < high:
            mid = (low + high) // 2
            if valid[mid] < left:
                low = mid + 1
            else:
                high = mid
        start = low

        # Find the last valid element <= right
        low, high = 0, len(valid)
        while low < high:
            mid = (low + high) // 2
            if valid[mid] <= right:
                low = mid + 1
            else:
                high = mid
        end = high

        if start >= end:
            results.append(0)
        else:
            # The answer is the number of elements in [start, end-1]
            results.append(end - start)

    return results
```