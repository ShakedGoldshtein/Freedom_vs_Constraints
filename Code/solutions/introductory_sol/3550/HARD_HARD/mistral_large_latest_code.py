```python
import math
from typing import List, Union

def sum_square_even_root_odd(nums: List[Union[int, float]]) -> float:
    """
    Processes a list of non-negative numbers by squaring even numbers and taking the square root
    of odd numbers, then returns the sum of the processed values rounded to two decimal places.

    Args:
        nums: A list of non-negative numbers (integers or floats).

    Returns:
        The sum of processed values, rounded to two decimal places.

    Raises:
        ValueError: If any number in the list is negative.
    """
    if not nums:
        raise ValueError("Input list cannot be empty")

    processed = []
    for num in nums:
        if num < 0:
            raise ValueError(f"Negative number found: {num}")
        if num == 0:
            processed.append(0.0)
        elif is_even(num):
            processed.append(num ** 2)
        else:
            processed.append(math.sqrt(num))

    total = sum(processed)
    return round(total, 2)

def is_even(num: Union[int, float]) -> bool:
    """
    Checks if a number is even, handling both integers and floats correctly.

    Args:
        num: The number to check.

    Returns:
        True if the number is even, False otherwise.
    """
    integer_part = int(round(num))
    return integer_part % 2 == 0
```