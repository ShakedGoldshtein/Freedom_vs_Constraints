```python
import numpy

def solve(dimensions):
    shape = tuple(map(int, dimensions.split()))
    zeros_array = numpy.zeros(shape, dtype=numpy.int)
    ones_array = numpy.ones(shape, dtype=numpy.int)
    return (zeros_array, ones_array)
```