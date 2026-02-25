```python
def sum_positive_numbers(numbers):
    """
    Calculate the sum of all positive numbers in the given array.
    
    Args:
        numbers: List of numbers (can be integers, floats, or mixed)
    
    Returns:
        float: Sum of all positive numbers in the array. Returns 0 if array is empty
               or contains no positive numbers.
    """
    if not numbers:
        return 0
    
    return sum(num for num in numbers if num > 0)
```