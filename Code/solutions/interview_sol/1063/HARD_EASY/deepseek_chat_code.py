```python
def solve(T, test_cases):
    """
    Find the remainder when A is divided by B for each test case.
    
    Args:
        T (int): Number of test cases
        test_cases (list): List of tuples (A, B) for each test case
    
    Returns:
        list: List of remainders for each test case
    """
    if not isinstance(T, int) or T < 1 or T > 1000:
        raise ValueError("T must be an integer between 1 and 1000")
    
    if len(test_cases) != T:
        raise ValueError("Number of test cases must equal T")
    
    results = []
    for A, B in test_cases:
        if not isinstance(A, int) or not isinstance(B, int):
            raise ValueError("A and B must be integers")
        
        if A < 1 or A > 10000 or B < 1 or B > 10000:
            raise ValueError("A and B must be between 1 and 10000")
        
        if B == 0:
            raise ValueError("Division by zero is not allowed")
        
        remainder = A % B
        results.append(remainder)
    
    return results
```