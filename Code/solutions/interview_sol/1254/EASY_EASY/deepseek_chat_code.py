```python
def solve(T, test_cases):
    results = []
    for i in range(T):
        N, P = test_cases[i][0]
        arr = test_cases[i][1]
        
        cakewalk_threshold = P // 2
        hard_threshold = P // 10
        
        cakewalk_count = 0
        hard_count = 0
        
        for participants in arr:
            if participants >= cakewalk_threshold:
                cakewalk_count += 1
            elif participants <= hard_threshold:
                hard_count += 1
        
        if cakewalk_count == 1 and hard_count == 2:
            results.append("yes")
        else:
            results.append("no")
    
    return results
```