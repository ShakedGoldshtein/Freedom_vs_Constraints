```python
def find_kth_bit(n: int, k: int) -> str:
    """
    Finds the k-th bit in the binary string Sn.

    Sn is formed as follows:
    S1 = "0"
    Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1

    Where '+' denotes concatenation, reverse(x) returns the reversed string x,
    and invert(x) inverts all bits in x (0 changes to 1, 1 changes to 0).

    This function utilizes a recursive approach to determine the k-th bit
    without explicitly constructing the string Sn, achieving optimal time
    and space complexity relative to n.

    Args:
        n: A positive integer representing the string index (1 <= n <= 20).
        k: A positive integer representing the 1-indexed position of the bit
           to find (1 <= k <= 2^n - 1).

    Returns:
        The k-th bit of Sn as a string ("0" or "1").
    """
    return _find_kth_bit_recursive(n, k)


def _find_kth_bit_recursive(current_n: int, k: int) -> str:
    """
    Recursive helper function to determine the k-th bit of Sn.

    Args:
        current_n: The current level of 'S' string being considered (e.g., for S_current_n).
        k: The 1-indexed position of the bit to find within S_current_n.

    Returns:
        The k-th bit of S_current_n as a string ("0" or "1").
    """
    if current_n == 1:
        # Base case: S1 = "0". The only bit is "0".
        return "0"

    # The length of Sn is 2^n - 1.
    # The middle character of Sn is always '1' and is located at index 2^(n-1).
    # This is equivalent to 1 << (n-1) using bit shift.
    mid_idx = 1 << (current_n - 1)

    if k == mid_idx:
        # If k is the middle index, the bit is '1'.
        return "1"
    elif k < mid_idx:
        # If k is in the first part (Si-1), we recursively look for the k-th bit in S(n-1).
        return _find_kth_bit_recursive(current_n - 1, k)
    else:
        # If k is in the third part (reverse(invert(Si-1))), we need to adjust k.
        # The k-th bit in Sn corresponds to the (k - mid_idx)-th bit in reverse(invert(S(n-1))).
        # Let m = k - mid_idx. This is the 1-indexed position in the reversed string.
        # The length of S(n-1) is (1 << (current_n - 1)) - 1.
        # The m-th bit of reverse(X) is the (length(X) - m + 1)-th bit of X.
        # So, the new_k for S(n-1) is:
        # new_k = (length(S(n-1))) - (k - mid_idx) + 1
        # new_k = ((1 << (current_n - 1)) - 1) - (k - (1 << (current_n - 1))) + 1
        # new_k = (1 << (current_n - 1)) - 1 - k + (1 << (current_n - 1)) + 1
        # new_k = 2 * (1 << (current_n - 1)) - k
        # new_k = (1 << current_n) - k
        new_k = (1 << current_n) - k

        # Recursively find the bit in S(n-1) using the adjusted k.
        bit_in_prev_s = _find_kth_bit_recursive(current_n - 1, new_k)

        # Since it was in the inverted part, invert the found bit.
        return "1" if bit_in_prev_s == "0" else "0"
```