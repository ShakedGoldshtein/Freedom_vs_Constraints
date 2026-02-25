```python
import math
from functools import reduce

def compute_gcd(arr):
    return reduce(math.gcd, arr)

def max_gcd_after_operations(arr):
    n = len(arr)
    if n == 1:
        return arr[0]

    max_gcd = 0

    # Case 1: No removal, just reverse (but GCD remains same as original)
    current_gcd = compute_gcd(arr)
    max_gcd = max(max_gcd, current_gcd)

    # Case 2: Remove a prefix and reverse the remaining
    for i in range(1, n):
        subarray = arr[i:]
        reversed_sub = subarray[::-1]
        current_gcd = compute_gcd(reversed_sub)
        max_gcd = max(max_gcd, current_gcd)

    # Case 3: Remove a suffix and reverse the remaining
    for i in range(1, n):
        subarray = arr[:n-i]
        reversed_sub = subarray[::-1]
        current_gcd = compute_gcd(reversed_sub)
        max_gcd = max(max_gcd, current_gcd)

    # Case 4: Remove a middle subarray and reverse the remaining
    # The remaining array is arr[0..i] + arr[j..n-1], then reversed
    for i in range(n):
        for j in range(i + 2, n + 1):
            left = arr[:i]
            right = arr[j:]
            combined = left + right
            if not combined:
                continue
            reversed_combined = combined[::-1]
            current_gcd = compute_gcd(reversed_combined)
            max_gcd = max(max_gcd, current_gcd)

    return max_gcd

def solve(test_cases):
    results = []
    for case in test_cases:
        n, arr = case
        results.append(max_gcd_after_operations(arr))
    return results
```