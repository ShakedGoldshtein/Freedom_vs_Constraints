```python
def iq_test(numbers_str):
    """
    Finds the position of the number that differs in evenness from the others.

    Args:
        numbers_str (str): A string of space-separated integers.

    Returns:
        int: The 1-based index of the number that is different in evenness.
    """
    numbers = [int(n) for n in numbers_str.split()]

    even_indices = []
    odd_indices = []

    for i, num in enumerate(numbers):
        # Check evenness and store 1-based index
        if num % 2 == 0:
            even_indices.append(i + 1)
        else:
            odd_indices.append(i + 1)

    # The problem guarantees there will be one number that differs.
    # So, either one group will have a single element, or the other will.
    if len(even_indices) == 1:
        return even_indices[0]
    else:  # len(odd_indices) == 1
        return odd_indices[0]

```