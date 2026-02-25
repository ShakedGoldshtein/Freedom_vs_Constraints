```python
import math


def sum_square_even_root_odd(nums: list[float]) -> float:
    """
    This function takes a list of numbers, squares the even numbers,
    takes the square root of the odd numbers, and returns the sum of the new list
    rounded to two decimal places.

    Args:
        nums (list): A list of non-negative numbers.

    Returns:
        float: The sum of the transformed list, rounded to two decimal places.
    """

    def transform_number(num: float) -> float:
        """
        Helper function to transform a single number: squares it if even, takes sqrt if odd.

        Args:
            num (float): A non-negative number.

        Returns:
            float: The transformed number.
        """
        if num % 2 == 0:
            return num**2
        else:
            return math.sqrt(num)

    # Apply the transformation to each number in the list and sum the results
    total = sum(transform_number(num) for num in nums)

    # Round the total to two decimal places
    return round(total, 2)
```