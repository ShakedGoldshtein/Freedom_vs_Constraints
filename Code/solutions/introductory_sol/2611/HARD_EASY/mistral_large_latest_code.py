```python
import numpy as np
from typing import Tuple, List

def create_arrays(shape_str: str) -> Tuple[np.ndarray, np.ndarray]:
    """
    Creates zero-filled and one-filled numpy arrays of given shape with integer type.

    Args:
        shape_str: Space-separated string of integers representing array dimensions.

    Returns:
        Tuple of (zero_array, one_array) as numpy arrays with dtype=int.
    """
    shape = tuple(int(dim) for dim in shape_str.split())
    zero_array = np.zeros(shape, dtype=np.int)
    one_array = np.ones(shape, dtype=np.int)
    return zero_array, one_array
```