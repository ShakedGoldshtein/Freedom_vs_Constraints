```python
import numpy as np

def print_arrays(*dimensions):
    zeros_array = np.zeros(dimensions, dtype = np.int)
    ones_array = np.ones(dimensions, dtype = np.int)
    return zeros_array, ones_array
```