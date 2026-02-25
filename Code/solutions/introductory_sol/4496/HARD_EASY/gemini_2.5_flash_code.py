```python
def hamming_distance(a: str, b: str) -> int:
    """
    Calculates the Hamming distance between two equal-length binary strings.

    The Hamming distance is the number of positions at which the corresponding
    characters differ. This function assumes the input strings are of equal
    length and contain only '0's and '1's, as per the problem description.

    Args:
        a: The first binary string.
        b: The second binary string, which must be of the same length as `a`.

    Returns:
        The Hamming distance as an integer.

    Time Complexity: O(N), where N is the length of the input strings.
                     The function iterates through each character of the strings once.
    Space Complexity: O(1), as only a single counter variable is used regardless
                      of the input string length.
    """
    distance = 0
    # The problem guarantees equal-length strings.
    # We iterate through the strings, comparing characters at each position.
    for i in range(len(a)):
        if a[i] != b[i]:
            distance += 1
    return distance
```