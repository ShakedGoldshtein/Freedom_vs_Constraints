```python
def hamming_distance(a: str, b: str) -> int:
    """
    Calculate the Hamming distance between two binary strings of equal length.
    
    Args:
        a: First binary string containing only 0s and 1s
        b: Second binary string containing only 0s and 1s
        
    Returns:
        Integer representing the Hamming distance
        
    Raises:
        ValueError: If strings are not of equal length
    """
    if len(a) != len(b):
        raise ValueError("Strings must be of equal length")
        
    return sum(c1 != c2 for c1, c2 in zip(a, b))
```