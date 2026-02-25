```python
def minOperations(n: int) -> int:
    """
    Calculates minimum operations needed to make all elements equal in array arr[i] = 2*i + 1
    Time: O(1), Space: O(1)
    """
    # For odd n: Each element needs (n-1)/2 moves to get to middle value
    # For even n: Each element needs n/2 moves to get to middle value
    # Sum of arithmetic sequence from 1 to floor(n/2)
    
    if n <= 1:
        return 0
        
    # For both odd/even n, result is floor(n/2) * ceil(n/2)
    return (n // 2) * ((n + 1) // 2)
```