```python
import math
from math import gcd

def compute_prefix_gcd(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = gcd(prefix[i-1], arr[i])
    return prefix

def compute_suffix_gcd(arr):
    n = len(arr)
    suffix = [0] * n
    suffix[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        suffix[i] = gcd(suffix[i+1], arr[i])
    return suffix

def solve_test_case(n, arr):
    if n == 1:
        return arr[0]
    
    prefix_gcd = compute_prefix_gcd(arr)
    suffix_gcd = compute_suffix_gcd(arr)
    
    max_gcd = 0
    
    for i in range(n):
        if i == 0:
            current_gcd = suffix_gcd[1]
        elif i == n-1:
            current_gcd = prefix_gcd[n-2]
        else:
            current_gcd = gcd(prefix_gcd[i-1], suffix_gcd[i+1])
        max_gcd = max(max_gcd, current_gcd)
    
    reversed_arr = arr[::-1]
    prefix_gcd_rev = compute_prefix_gcd(reversed_arr)
    suffix_gcd_rev = compute_suffix_gcd(reversed_arr)
    
    for i in range(n):
        if i == 0:
            current_gcd = suffix_gcd_rev[1]
        elif i == n-1:
            current_gcd = prefix_gcd_rev[n-2]
        else:
            current_gcd = gcd(prefix_gcd_rev[i-1], suffix_gcd_rev[i+1])
        max_gcd = max(max_gcd, current_gcd)
    
    return max_gcd

def main(T, test_cases):
    results = []
    for i in range(T):
        n = test_cases[i][0]
        arr = test_cases[i][1]
        results.append(solve_test_case(n, arr))
    return results
```