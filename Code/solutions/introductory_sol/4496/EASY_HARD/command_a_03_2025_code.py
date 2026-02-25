```python
def hamming_distance(a: str, b: str) -> int:
    """
    Calculate the Hamming distance between two binary strings.

    The Hamming distance is the number of positions at which the corresponding bits are different.

    Args:
        a (str): The first binary string.
        b (str): The second binary string.

    Returns:
        int: The Hamming distance between the two strings.
    """
    return sum(c1 != c2 for c1, c2 in zip(a, b))
```