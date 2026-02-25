```python
def disarium_number(num):
    """
    Check if a number is a Disarium number.
    A Disarium number is one where sum of digits powered by their position equals the number.
    
    Args:
        num: Positive integer to check
        
    Returns:
        String "Disarium !!" if number is Disarium, "Not !!" if not
    """
    # Convert number to string to process digits
    num_str = str(num)
    
    # Calculate sum of digits powered by position
    digit_sum = sum(int(d) ** (i+1) for i, d in enumerate(num_str))
    
    # Compare sum to original number
    if digit_sum == num:
        return "Disarium !!"
    return "Not !!"
```