```python
import math


def sum_square_even_root_odd(nums: list[float]) -> float:
    """
    This function takes a list of numbers, squares the even numbers,
    takes the square root of the odd numbers, and returns the sum
    of the resulting list, rounded to two decimal places.

    Args:
        nums (list): A list of non-negative numbers.

    Returns:
        float: The sum of the transformed list, rounded to two decimal places.
    """
    # Use list comprehension to apply the transformation to each number in the list
    transformed_nums = [
        num**2 if num % 2 == 0 else math.sqrt(num) for num in nums
    ]

    # Calculate the sum of the transformed list and round to two decimal places
    result = round(sum(transformed_nums), 2)

    return result
```