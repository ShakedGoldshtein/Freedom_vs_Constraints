```python
def is_monotonic(A):
    """
    Check if an array is monotonic (either entirely non-increasing or non-decreasing).
    
    Args:
        A: List of integers to check for monotonicity.
    
    Returns:
        bool: True if the array is monotonic, False otherwise.
    """
    if not A or len(A) <= 1:
        return True
    
    increasing = decreasing = True
    
    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            decreasing = False
        if A[i] < A[i-1]:
            increasing = False
            
        if not increasing and not decreasing:
            return False
            
    return increasing or decreasing
```