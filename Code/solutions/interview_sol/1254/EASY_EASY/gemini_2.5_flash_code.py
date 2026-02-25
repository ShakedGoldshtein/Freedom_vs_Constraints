```python
def solve(N, P, solving_counts):
    cakewalk_threshold = P // 2
    hard_threshold = P // 10

    cakewalk_count = 0
    hard_count = 0

    for count in solving_counts:
        # Check for cakewalk difficulty
        if count >= cakewalk_threshold:
            cakewalk_count += 1
        # Check for hard difficulty
        if count <= hard_threshold:
            hard_count += 1
    
    # A contest is balanced if it has exactly 1 cakewalk and exactly 2 hard problems
    if cakewalk_count == 1 and hard_count == 2:
        return "yes"
    else:
        return "no"

```