```python
import numpy as np


def solve(shape):
    """
    Returns two numpy arrays of the given shape, one filled with zeros and the other with ones.

    Parameters:
    shape (tuple): A tuple of integers representing the shape of the arrays.

    Returns:
    tuple: A tuple containing two numpy arrays, the first filled with zeros and the second with ones.
    """
    zeros_array = np.zeros(shape, dtype=np.int)
    ones_array = np.ones(shape, dtype=np.int)
    return zeros_array, ones_array
```