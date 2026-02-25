```python
def is_balanced_contest(n: int, p: int, solved: list[int]) -> str:
    """
    Check if a contest is balanced based on problem difficulty distribution.
    A balanced contest has exactly 1 cakewalk and 2 hard problems.
    
    Args:
        n: Number of problems
        p: Number of participants
        solved: List of participants solving each problem
        
    Returns:
        'yes' if contest is balanced, 'no' otherwise
    """
    cakewalk = 0
    hard = 0
    
    half = p // 2
    tenth = p // 10
    
    for s in solved:
        if s >= half:
            cakewalk += 1
        if s <= tenth:
            hard += 1
            
    return 'yes' if cakewalk == 1 and hard == 2 else 'no'

def solve(t: int, test_cases: list[tuple[int, int, list[int]]]) -> list[str]:
    """
    Process multiple test cases to check if contests are balanced.
    
    Args:
        t: Number of test cases
        test_cases: List of tuples containing (n, p, solved) for each test case
        
    Returns:
        List of strings ('yes'/'no') for each test case
    """
    results = []
    for n, p, solved in test_cases:
        results.append(is_balanced_contest(n, p, solved))
    return results
```