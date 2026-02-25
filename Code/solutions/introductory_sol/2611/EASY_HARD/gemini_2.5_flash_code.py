```python
import numpy

def solve(shape_str):
    """
    Creates two NumPy arrays (one filled with zeros, one with ones) 
    of a specified shape and integer type.

    The shape is parsed from a space-separated string of integers.

    Args:
        shape_str (str): A string containing space-separated integers 
                         representing the dimensions of the array.
                         Example: "1 2 3"

    Returns:
        tuple: A tuple containing two numpy arrays.
               The first element is the zeros array, and the second 
               is the ones array, both of dtype=numpy.int.
    """
    dimensions = tuple(int(x) for x in shape_str.split())

    zeros_array = numpy.zeros(dimensions, dtype=numpy.int)
    ones_array = numpy.ones(dimensions, dtype=numpy.int)

    return (zeros_array, ones_array)

```