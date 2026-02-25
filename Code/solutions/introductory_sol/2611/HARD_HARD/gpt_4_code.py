```python
import numpy

def generate_arrays(dims):
    try:
        dims_list = [int(x) for x in dims.split()]
        
        if not all(1<=x<=3 for x in dims_list):
           return "Dimensions should exist between 1 and 3"
        
        zeros_array = numpy.zeros(tuple(dims_list), dtype=numpy.int)
        ones_array = numpy.ones(tuple(dims_list), dtype=numpy.int)
                
        return zeros_array, ones_array

    except ValueError:
        return "Dimensions must be integers"

    except Exception as e:
        return str(e)
```