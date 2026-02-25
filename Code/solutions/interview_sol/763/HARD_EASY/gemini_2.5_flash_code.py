```python
def can_convert_binary_strings(N: int, S: str, P: str) -> str:
    """
    Determines if binary string S can be converted to binary string P using
    a specific swap operation.

    The operation allows choosing two indices i and j (1-indexed, 1 <= i < j <= N)
    such that S_i is '1' and S_j is '0', and swapping S_i with S_j.
    This implies that a '1' can only move to the right (to a higher index),
    and a '0' can only move to the left (to a lower index).

    For S to be convertible to P, two conditions must be met:
    1. The total count of '1's in S must be equal to the total count of '1's in P,
       as the swap operation preserves the count of '1's and '0's.
    2. For any prefix of the string S (from index 0 to k, for all k < N),
       the number of '1's in that prefix must be greater than or equal to the
       number of '1's in the corresponding prefix of P. This is because '1's
       can only move to the right; they cannot move into a prefix from a
       position outside and to its right.

    Args:
        N: The length of the binary strings S and P.
        S: The source binary string.
        P: The target binary string.

    Returns:
        "Yes" if S can be converted to P, "No" otherwise.
    """
    current_ones_s = 0
    current_ones_p = 0

    # Iterate through the strings from left to right, maintaining prefix counts of '1's
    for i in range(N):
        if S[i] == '1':
            current_ones_s += 1
        if P[i] == '1':
            current_ones_p += 1

        # Check condition 2: The number of '1's in S's prefix must be >= P's prefix
        if current_ones_s < current_ones_p:
            return "No"

    # After iterating through the entire strings (up to index N-1),
    # current_ones_s and current_ones_p hold the total count of '1's in S and P, respectively.
    # Check condition 1: Total count of '1's must be equal.
    # If the loop finished without returning "No", it means current_ones_s >= current_ones_p
    # for all prefixes. If the total counts are not equal, then current_ones_s must be
    # strictly greater than current_ones_p at the end. In this case, conversion is impossible.
    if current_ones_s != current_ones_p:
        return "No"

    # If both conditions are met throughout the iteration and at the end, conversion is possible.
    return "Yes"
```