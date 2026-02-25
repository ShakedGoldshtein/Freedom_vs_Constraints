```python
from collections import defaultdict
from bisect import bisect_left
 
def count_beautiful_subarrays(A, K):
    N = len(A)
    prefix_counts = [defaultdict(int) for _ in range(N+1)]
    prefix_counts[0][0] = 1
    prefix_sum = 0
    for i in range(N):
        prefix_sum += A[i]
        prefix_counts[i+1] = prefix_counts[i].copy()
        prefix_counts[i+1][prefix_sum] += 1
    total_beautiful_subarrays = 0
    for R in range(N):
        # Subarray from L to R is beautiful, if the number of elements in it is K times the number of elements with the value X.
        # Thus, for each R, we need to find how many prefixes sum to prefix[R] - KX, for each X from 1 to K.
        # X >= prefix[R] / K is needed, as otherwise KX > prefix[R] isn't possible.
        for X in range(1, min(K, R//K + 2)):
            total_beautiful_subarrays += prefix_counts[R+1][prefix_sum[K*R] - K*X]
    return total_beautiful_subarrays
  
def solve(T, test_cases):
    result = []
    for t in range(T):
        N, K, A = test_cases[t]
        result.append(count_beautiful_subarrays(A, K))
    return result
```
