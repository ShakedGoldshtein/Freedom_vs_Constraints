```python
def sum_positives(numbers: list[int]) -> int:
    """
    Returns the sum of all positive numbers in the given list.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        int: The sum of all positive numbers in the list. If no positive numbers are present, returns 0.
    """
    return sum(num for num in numbers if num > 0)
```