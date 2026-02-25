```python
import numpy as np


def solve(shape_str: str) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate zero and one arrays based on the given shape.

    Parameters:
    shape_str (str): A string of space-separated integers representing the shape of the array.

    Returns:
    tuple: A tuple containing two numpy arrays, the first filled with zeros and the second with ones.
    """
    # Parse the input string into a tuple of integers representing the shape
    shape = tuple(map(int, shape_str.split()))

    # Create an array of zeros with the given shape and integer type
    zeros_array = np.zeros(shape, dtype=np.int)

    # Create an array of ones with the given shape and integer type
    ones_array = np.ones(shape, dtype=np.int)

    return zeros_array, ones_array
```