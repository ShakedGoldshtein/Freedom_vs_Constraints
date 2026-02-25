```python
def solve_single_case(N, A):
    # Sort array to get min/max values easily
    A.sort()
    
    # For maximum difference, pair smallest with largest numbers
    result = 0
    for i in range(0, N, 2):
        # Take N/2 pairs from both ends
        result += abs(A[i] - A[N-1-i])
        
    return result

def solve(T, test_cases):
    """
    Solves multiple test cases
    Args:
        T: Number of test cases
        test_cases: List of tuples (N, A) where N is array size and A is array
    Returns:
        List of maximum achievable sums for each test case
    """
    results = []
    
    for N, A in test_cases:
        results.append(solve_single_case(N, list(A)))
        
    return results
```