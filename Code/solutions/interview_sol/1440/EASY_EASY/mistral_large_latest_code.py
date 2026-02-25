```python
def solve(test_cases):
    results = []
    for case in test_cases:
        N, A = case
        A_sorted = sorted(A)
        max_cost = 0
        # Try the largest element at the end
        for i in range(N):
            if A_sorted[i] == max(A_sorted):
                perm = A_sorted[:i] + A_sorted[i+1:] + [A_sorted[i]]
                current = perm[0]
                for num in perm[1:]:
                    current %= num
                if current > max_cost:
                    max_cost = current
        # Try the second largest element at the end
        if N >= 2:
            second_max = sorted(A_sorted)[-2]
            for i in range(N):
                if A_sorted[i] == second_max:
                    perm = A_sorted[:i] + A_sorted[i+1:] + [A_sorted[i]]
                    current = perm[0]
                    for num in perm[1:]:
                        current %= num
                    if current > max_cost:
                        max_cost = current
        # Try the largest element at the second last position
        if N >= 2:
            for i in range(N):
                if A_sorted[i] == max(A_sorted):
                    for j in range(N):
                        if j != i:
                            perm = A_sorted[:i] + A_sorted[i+1:j] + A_sorted[j+1:] + [A_sorted[i], A_sorted[j]]
                            current = perm[0]
                            for num in perm[1:]:
                                current %= num
                            if current > max_cost:
                                max_cost = current
        # Try the largest element at the start
        perm = [max(A_sorted)] + A_sorted[:-1]
        current = perm[0]
        for num in perm[1:]:
            current %= num
        if current > max_cost:
            max_cost = current
        results.append(max_cost)
    return results

def max_cost(test_cases):
    results = []
    for case in test_cases:
        N, A = case
        max_val = max(A)
        A_sorted = sorted(A)
        # The optimal permutation is either:
        # 1. The largest element at the end, or
        # 2. The largest element at the second last position, or
        # 3. The largest element at the start
        # We check all three cases
        candidates = []
        # Case 1: largest at end
        perm1 = A_sorted[:-1] + [max_val]
        current = perm1[0]
        for num in perm1[1:]:
            current %= num
        candidates.append(current)
        # Case 2: largest at second last
        if N >= 2:
            second_last_pos = N - 2
            perm2 = A_sorted[:second_last_pos] + [max_val] + A_sorted[second_last_pos:N-1] + [A_sorted[-1]]
            current = perm2[0]
            for num in perm2[1:]:
                current %= num
            candidates.append(current)
        # Case 3: largest at start
        perm3 = [max_val] + A_sorted[:-1]
        current = perm3[0]
        for num in perm3[1:]:
            current %= num
        candidates.append(current)
        # Also check the permutation with the largest element at the end and the second largest at the second last
        if N >= 2:
            second_max = max(A_sorted[:-1])
            perm4 = A_sorted[:-2] + [second_max] + [max_val]
            current = perm4[0]
            for num in perm4[1:]:
                current %= num
            candidates.append(current)
        results.append(max(candidates))
    return results

def solve_optimized(test_cases):
    results = []
    for case in test_cases:
        N, A = case
        max_val = max(A)
        A_sorted = sorted(A)
        # The maximum cost is either:
        # 1. The largest element itself (when it's first)
        # 2. The largest element mod the second largest (when largest is second)
        # 3. The largest element mod (second largest mod third largest) (when largest is third)
        # We check these cases
        candidates = []
        # Case 1: largest is first
        candidates.append(max_val)
        # Case 2: largest is second
        if N >= 2:
            second_max = max(A_sorted[:-