```python
import math
from collections import defaultdict

def solve(test_cases):
    results = []
    for case in test_cases:
        N, A = case
        freq = defaultdict(int)
        for num in A:
            freq[num] += 1

        min_cost = float('inf')
        best_length = 1

        for possible_length in range(1, max(A) + 1):
            total_cost = 0
            for length in freq:
                required_pieces = (length + possible_length - 1) // possible_length
                total_cost += required_pieces * freq[length]
            if total_cost < min_cost or (total_cost == min_cost and possible_length < best_length):
                min_cost = total_cost
                best_length = possible_length

        results.append((best_length, min_cost))
    return results
```