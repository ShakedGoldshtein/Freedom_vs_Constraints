```python
def solve(test_cases):
    results = []
    for _ in range(test_cases):
        n, p = test_cases[_][0]
        problems = test_cases[_][1]
        
        # Calculate thresholds
        cakewalk_threshold = p // 2
        hard_threshold = p // 10
        
        # Count problems by difficulty
        cakewalk_count = 0
        hard_count = 0
        
        for solvers in problems:
            if solvers >= cakewalk_threshold and solvers <= p:
                cakewalk_count += 1
            if solvers <= hard_threshold:
                hard_count += 1
                
        # Check if balanced
        if cakewalk_count == 1 and hard_count == 2:
            results.append("yes")
        else:
            results.append("no")
            
    return results
```