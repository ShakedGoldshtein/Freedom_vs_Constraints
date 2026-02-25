```python
import math
from functools import reduce

def compute_gcd(arr):
    return reduce(math.gcd, arr)

def solve(arr):
    n = len(arr)
    if n == 1:
        return arr[0]

    max_gcd = 0

    # Case 1: No removal, just reverse
    reversed_arr = arr[::-1]
    current_gcd = compute_gcd(reversed_arr)
    if current_gcd > max_gcd:
        max_gcd = current_gcd

    # Case 2: Remove a prefix
    for i in range(n):
        sub_arr = arr[i:]
        reversed_sub = sub_arr[::-1]
        current_gcd = compute_gcd(reversed_sub)
        if current_gcd > max_gcd:
            max_gcd = current_gcd

    # Case 3: Remove a suffix
    for i in range(1, n + 1):
        sub_arr = arr[:i]
        reversed_sub = sub_arr[::-1]
        current_gcd = compute_gcd(reversed_sub)
        if current_gcd > max_gcd:
            max_gcd = current_gcd

    # Case 4: Remove a middle subarray (i to j)
    for i in range(n):
        for j in range(i + 1, n):
            left = arr[:i]
            right = arr[j:]
            combined = left + right
            reversed_combined = combined[::-1]
            current_gcd = compute_gcd(reversed_combined)
            if current_gcd > max_gcd:
                max_gcd = current_gcd

    return max_gcd

def solve_test_cases(test_cases):
    results = []
    for case in test_cases:
        N, arr = case
        results.append(solve(arr))
    return results
```