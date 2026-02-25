```python
def hamming_distance(a: str, b: str) -> int:
    """
    Computes the Hamming distance between two equal-length binary strings.

    The Hamming distance is the number of positions at which the corresponding
    characters differ.

    Args:
        a: First binary string (composed of '0's and '1's).
        b: Second binary string (composed of '0's and '1's), same length as `a`.

    Returns:
        The Hamming distance between `a` and `b` as an integer.

    Raises:
        ValueError: If the input strings have unequal lengths or contain invalid characters.
    """
    if len(a) != len(b):
        raise ValueError("Input strings must be of equal length.")

    if not all(c in {'0', '1'} for c in a) or not all(c in {'0', '1'} for c in b):
        raise ValueError("Input strings must contain only '0's and '1's.")

    return sum(1 for x, y in zip(a, b) if x != y)
```