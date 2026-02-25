```python
def find_kth_bit(n: int, k: int) -> str:
    """
    Returns the k-th bit in the binary string S_n, where S_n is constructed recursively:
    S1 = "0"
    S_i = S_{i-1} + "1" + reverse(invert(S_{i-1})) for i > 1.

    Args:
        n: The index of the binary string (1 <= n <= 20).
        k: The 1-based position of the bit to retrieve (1 <= k <= 2^n - 1).

    Returns:
        The k-th bit in S_n as a string ("0" or "1").
    """
    def _invert_bit(bit: str) -> str:
        return "1" if bit == "0" else "0"

    def _get_bit(n: int, k: int) -> str:
        if n == 1:
            return "0"
        length = (1 << n) - 1
        mid = (length // 2) + 1
        if k == mid:
            return "1"
        elif k < mid:
            return _get_bit(n - 1, k)
        else:
            inverted_bit = _invert_bit(_get_bit(n - 1, length - k + 1))
            return inverted_bit

    return _get_bit(n, k)
```