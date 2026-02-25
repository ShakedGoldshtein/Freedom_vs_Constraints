```python
def solve(test_cases):
    """
    Add pairs of numbers for each test case
    Args:
        test_cases: List of tuples containing pairs of integers to add
    Returns:
        List containing sum for each test case
    """
    if not test_cases or len(test_cases) < 1 or len(test_cases) > 1000:
        return []
        
    result = []
    for a, b in test_cases:
        if not (0 <= a <= 10000 and 0 <= b <= 10000):
            continue
        result.append(a + b)
            
    return result
```