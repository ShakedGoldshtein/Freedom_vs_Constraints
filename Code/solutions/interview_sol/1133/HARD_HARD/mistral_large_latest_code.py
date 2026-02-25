```python
import math
from collections import defaultdict

def solve_wire_purchase(N, A):
    if N == 0 or not A:
        return (0, 0)

    max_A = max(A)
    min_cost = float('inf')
    best_length = 1

    # Precompute all possible divisors of all A[i] to limit candidate lengths
    divisors = defaultdict(set)
    for num in A:
        if num == 0:
            continue
        # Get all divisors of num
        for d in range(1, int(math.isqrt(num)) + 1):
            if num % d == 0:
                divisors[d].add(num)
                divisors[num // d].add(num)

    # Also consider all A[i] as potential lengths
    for num in A:
        divisors[num].add(num)

    # Check all candidate lengths (divisors of any A[i] or A[i] themselves)
    candidates = set()
    for d in divisors:
        candidates.add(d)
    for num in A:
        candidates.add(num)

    for L in sorted(candidates):
        if L == 0:
            continue
        total_cost = 0
        for num in A:
            if num % L != 0:
                total_cost = float('inf')
                break
            total_cost += num // L
        if total_cost < min_cost:
            min_cost = total_cost
            best_length = L
        elif total_cost == min_cost and L < best_length:
            best_length = L

    return (best_length, min_cost)

def solve(T, test_cases):
    results = []
    for case in test_cases:
        N, A = case
        results.append(solve_wire_purchase(N, A))
    return results
```