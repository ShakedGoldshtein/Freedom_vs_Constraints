```python
import bisect
from collections import defaultdict

def solve(T, test_cases):
    results = []
    for case in test_cases:
        N, Q, mountains, queries = case
        case_results = []
        # Preprocess the initial state
        height_to_indices = defaultdict(list)
        for idx, height in enumerate(mountains):
            height_to_indices[height].append(idx)
        # Process each query
        for query in queries:
            if query[0] == 0:  # Type 1: Update
                _, A, B = query
                old_height = mountains[A]
                if old_height != B:
                    # Remove old index from old_height's list
                    indices = height_to_indices[old_height]
                    pos = bisect.bisect_left(indices, A)
                    if pos < len(indices) and indices[pos] == A:
                        indices.pop(pos)
                    # Add new index to new_height's list
                    mountains[A] = B
                    bisect.insort(height_to_indices[B], A)
            else:  # Type 2: Query
                _, A = query
                current_height = mountains[A]
                res = -1
                # Check all possible heights greater than current_height
                for height in sorted(height_to_indices.keys()):
                    if height <= current_height:
                        continue
                    indices = height_to_indices[height]
                    # Find the first index > A
                    pos = bisect.bisect_right(indices, A)
                    if pos < len(indices):
                        candidate_idx = indices[pos]
                        # Verify no duplicates of this height before A
                        valid = True
                        for h in height_to_indices:
                            if h == height:
                                continue
                            if h == current_height:
                                continue
                            for idx in height_to_indices[h]:
                                if A < idx < candidate_idx:
                                    valid = False
                                    break
                            if not valid:
                                break
                        if valid:
                            res = height
                            break
                case_results.append(res)
        results.append(case_results)
    return results

def process_input(T, cases):
    test_cases = []
    for case in cases:
        N, Q, mountains, queries = case
        test_cases.append((N, Q, mountains.copy(), queries.copy()))
    return solve(T, test_cases)
```