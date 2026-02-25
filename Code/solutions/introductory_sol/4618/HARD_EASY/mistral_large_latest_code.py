```python
from typing import Iterable, Union

Number = Union[int, float]

def sum_positives(numbers: Iterable[Number]) -> Number:
    """
    Sums all positive numbers in the given iterable.

    Args:
        numbers: An iterable of numbers (int or float).

    Returns:
        The sum of all positive numbers in the input. Returns 0 if no positive numbers exist.
    """
    return sum(num for num in numbers if num > 0)
```