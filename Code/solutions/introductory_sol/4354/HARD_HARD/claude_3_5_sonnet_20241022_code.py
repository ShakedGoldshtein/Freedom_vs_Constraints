```python
def padovan(n: int) -> int:
    """
    Calculate the nth Padovan number using dynamic programming.
    Time complexity: O(n)
    Space complexity: O(1)
    
    Args:
        n: Non-negative integer index of Padovan number to calculate
        
    Returns:
        The nth Padovan number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
        
    if n <= 2:
        return 1
        
    # Use rolling window of size 3 to calculate next number
    p0, p1, p2 = 1, 1, 1
    
    for _ in range(3, n + 1):
        p0, p1, p2 = p1, p2, p0 + p1
        
    return p2
```