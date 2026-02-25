```python
def findKthBit(n: int, k: int) -> str:
    """
    Returns the kth bit in the binary string Sn.

    Args:
    n (int): The index of the binary string in the sequence.
    k (int): The position of the bit to find (1-indexed).

    Returns:
    str: The kth bit in Sn, either '0' or '1'.
    """

    def generate_s(n: int) -> str:
        """
        Generates the nth binary string in the sequence.

        Args:
        n (int): The index of the binary string to generate.

        Returns:
        str: The nth binary string in the sequence.
        """
        if n == 1:
            return "0"
        prev = generate_s(n - 1)
        inverted = ''.join('1' if bit == '0' else '0' for bit in prev)
        return prev + "1" + inverted[::-1]

    s = generate_s(n)
    return s[k - 1]
```