```python
def is_balanced_contest(test_cases):
    results = []
    for case in test_cases:
        N, P, solves = case
        cakewalk_threshold = P // 2
        hard_threshold = P // 10
        cakewalk = 0
        hard = 0
        for s in solves:
            if s >= cakewalk_threshold:
                cakewalk += 1
            elif s <= hard_threshold:
                hard += 1
        if cakewalk == 1 and hard == 2:
            results.append("yes")
        else:
            results.append("no")
    return results
```