```python
def hamming_distance(a, b):
    """
    Calculates the Hamming distance between two equal-length binary strings.

    The Hamming distance is the number of positions at which the corresponding
    characters are different.

    Args:
        a (str): The first binary string.
        b (str): The second binary string, of equal length to 'a'.

    Returns:
        int: The Hamming distance between the two strings.
    """
    # The sum function with a generator expression provides a concise
    # and efficient way to count differences.
    # It iterates through corresponding characters of both strings (using zip)
    # and increments the count (adds 1) for each position where characters differ.
    return sum(1 for char_a, char_b in zip(a, b) if char_a != char_b)
```