```python
def solve(N, S, P):
    """
    Determines if binary string S can be converted to binary string P using
    the specified operation.

    The operation allows swapping S_i ('1') with S_j ('0') where i < j.
    This means a '1' can only move to the right (to a '0' position)
    and a '0' can only move to the left (to a '1' position).

    This implies two critical conditions for conversion to be possible:
    1. The total number of '1's in S and P must be the same. If they differ,
       it's impossible as operations don't change character counts.
    2. Since '1's can only move to the right, the k-th '1' in S (when considering
       '1's by their original index) must be at an index less than or equal to
       the index of the k-th '1' in P. If any '1' needs to move to its left,
       it's impossible.

    Args:
        N (int): The length of strings S and P.
        S (str): The initial binary string.
        P (str): The target binary string.

    Returns:
        str: "Yes" if S can be converted to P, "No" otherwise.
    """

    # Extract the 0-indexed positions of '1's in string S
    idx_S_ones = [i for i, char in enumerate(S) if char == '1']

    # Extract the 0-indexed positions of '1's in string P
    idx_P_ones = [i for i, char in enumerate(P) if char == '1']

    # Condition 1: Check if the total count of '1's is the same
    if len(idx_S_ones) != len(idx_P_ones):
        return "No"

    # Condition 2: Check if each '1' in S can reach its target position in P
    # Iterate through the lists of '1's positions (which are already sorted by index)
    for i in range(len(idx_S_ones)):
        # If the i-th '1' in S is at a position greater than the i-th '1' in P,
        # it means it would have to move to the left, which is not allowed.
        if idx_S_ones[i] > idx_P_ones[i]:
            return "No"

    # If both conditions are met, it is possible to convert S to P.
    return "Yes"

```