```python
def disarium_number(n):
    """
    Check if a number is a Disarium number.
    
    A Disarium number is a number that is equal to the sum of its digits 
    each raised to the power of their respective positions.
    
    Args:
        n: Positive integer to check
        
    Returns:
        str: "Disarium !!" if n is Disarium, "Not !!" otherwise
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a positive integer")
    
    digits = [int(d) for d in str(n)]
    total = sum(digit ** (i + 1) for i, digit in enumerate(digits))
    
    return "Disarium !!" if total == n else "Not !!"
```