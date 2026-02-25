```python
def is_balanced_contest(N, P, solves):
    cakewalk_threshold = P // 2
    hard_threshold = P // 10

    cakewalk_count = 0
    hard_count = 0

    for solve in solves:
        if solve >= cakewalk_threshold:
            cakewalk_count += 1
        elif solve <= hard_threshold:
            hard_count += 1

    return cakewalk_count == 1 and hard_count == 2

def solve(T, test_cases):
    results = []
    for case in test_cases:
        N, P, solves = case
        balanced = is_balanced_contest(N, P, solves)
        results.append("yes" if balanced else "no")
    return results
```