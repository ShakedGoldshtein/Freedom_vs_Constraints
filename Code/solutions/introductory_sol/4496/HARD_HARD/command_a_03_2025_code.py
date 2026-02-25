```python
def hamming_distance(a: str, b: str) -> int:
    """
    Calculate the Hamming distance between two binary strings of equal length.

    The Hamming distance is the number of positions at which the corresponding bits are different.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        int: The Hamming distance between the two strings.

    Raises:
        ValueError: If the input strings are not of equal length.
    """
    if len(a) != len(b):
        raise ValueError("Input strings must be of equal length")

    return sum(el1 != el2 for el1, el2 in zip(a, b))
```