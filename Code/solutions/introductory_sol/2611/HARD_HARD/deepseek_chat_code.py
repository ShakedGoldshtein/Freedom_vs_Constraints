```python
import numpy

def generate_arrays(dimensions):
    shape = tuple(dimensions)
    zeros_array = numpy.zeros(shape, dtype=numpy.int)
    ones_array = numpy.ones(shape, dtype=numpy.int)
    return zeros_array, ones_array

def solve(input_string):
    dimensions = list(map(int, input_string.split()))
    zeros_result, ones_result = generate_arrays(dimensions)
    return zeros_result, ones_result
```