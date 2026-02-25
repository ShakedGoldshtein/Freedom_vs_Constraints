```python
import numpy

def create_zeros_and_ones_arrays(shape_str: str) -> tuple[numpy.ndarray, numpy.ndarray]:
    """
    Creates two NumPy arrays: one filled with zeros and one filled with ones,
    both having the shape specified by the input string and an integer data type.

    The input string should contain space-separated integers, each representing
    the size of a dimension.

    Args:
        shape_str: A string containing space-separated integers representing
                   the dimensions of the desired arrays (e.g., "1 2", "3 1 2").

    Returns:
        A tuple containing two numpy.ndarray objects:
        - The first array is filled with zeros.
        - The second array is filled with ones.
        Both arrays have the specified shape and dtype=numpy.int.

    Raises:
        TypeError: If the input 'shape_str' is not a string.
        ValueError: If the shape_str is empty, contains non-integer values,
                    results in an empty set of dimensions, or if any dimension
                    is outside the allowed range [1, 3] as per problem constraints.
    """
    if not isinstance(shape_str, str):
        raise TypeError("Input 'shape_str' must be a string.")
    
    # Process the string to get individual dimension strings
    # .strip() removes leading/trailing whitespace, and .split() handles multiple spaces
    dimension_strings = shape_str.strip().split()

    # Handle cases where the input string might lead to no dimensions
    if not dimension_strings:
        raise ValueError("Input 'shape_str' cannot be empty or consist only of spaces, "
                         "and must specify at least one dimension.")

    try:
        # Parse each dimension string to an integer and form a tuple for NumPy shape
        shape_dimensions = tuple(int(dim) for dim in dimension_strings)
        
        # Validate dimensions against the problem constraints (1 <= each integer <= 3)
        for dim in shape_dimensions:
            if not (1 <= dim <= 3):
                raise ValueError(f"Each dimension must be an integer between 1 and 3, "
                                 f"inclusive, but found {dim}.")

    except ValueError as e:
        # Catch errors from int() conversion or custom dimension validation
        raise ValueError(f"Invalid shape string format or dimension value: {e}. "
                         "Expected space-separated integers.") from e
    
    # Create the array of zeros with the specified shape and integer type
    zeros_array = numpy.zeros(shape_dimensions, dtype=numpy.int)

    # Create the array of ones with the specified shape and integer type
    ones_array = numpy.ones(shape_dimensions, dtype=numpy.int)

    return zeros_array, ones_array
```