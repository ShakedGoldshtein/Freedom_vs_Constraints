```python
import numpy

def solve(dimensions):
    shape = tuple(map(int, dimensions.split()))
    zeros_array = numpy.zeros(shape, dtype=int)
    ones_array = numpy.ones(shape, dtype=int)
    return zeros_array, ones_array
```