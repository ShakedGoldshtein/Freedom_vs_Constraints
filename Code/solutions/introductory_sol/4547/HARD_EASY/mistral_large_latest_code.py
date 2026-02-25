```python
def more_zeros(s: str) -> list[str]:
    """
    Returns a list of characters from the input string whose ASCII binary representation
    has more zeros than ones, with duplicates removed while preserving first occurrence order.

    Args:
        s: Input string of length > 0.

    Returns:
        List of qualifying characters in order of first appearance.
    """
    def count_bits(n: int) -> tuple[int, int]:
        """Counts the number of zeros and ones in the binary representation of n."""
        zeros = 0
        ones = 0
        while n > 0:
            if n & 1:
                ones += 1
            else:
                zeros += 1
            n >>= 1
        return (zeros, ones)

    seen = set()
    result = []

    for char in s:
        if char in seen:
            continue
        ascii_val = ord(char)
        zeros, ones = count_bits(ascii_val)
        if zeros > ones:
            result.append(char)
            seen.add(char)

    return result
```