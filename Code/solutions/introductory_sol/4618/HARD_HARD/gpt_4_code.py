```python
def sum_positive_numbers(numbers):
    """
    Function that returns the sum of all positive numbers in a provided list.
    """
    try:
        return sum(num for num in numbers if num > 0)
    except TypeError:
        return "Error: Input should be a list of integers"
```