```python
def solve(N, K, M, A):
    """
    Finds the number of subsequences of array A of length K
    which satisfy the property S_i % M = i % M for 1 <= i <= K.

    Args:
        N: The length of the array A.
        K: The required length of the subsequence.
        M: The modulo value.
        A: A list of N non-negative integers.

    Returns:
        The number of valid subsequences modulo 1000000007.
    """
    
    MOD = 1000000007

    # dp[j] stores the number of valid subsequences of length j found so far.
    # dp[0] is initialized to 1, representing one way to form an empty subsequence.
    dp = [0] * (K + 1)
    dp[0] = 1

    # Iterate through each element 'x' in the input array A
    for x in A:
        # Iterate through possible subsequence lengths from K down to 1.
        # This order is crucial to ensure that dp[j-1] used in the calculation
        # for dp[j] refers to counts from previous elements, not including
        # the current element 'x' as its (j-1)-th element.
        for j in range(K, 0, -1):
            # Check if the current element 'x' can be the j-th element (S_j)
            # of a valid subsequence. The condition is S_j % M == j % M.
            if x % M == j % M:
                # If it can, 'x' can extend any valid subsequence of length j-1
                # to form a new valid subsequence of length j.
                # dp[j-1] holds the count of such valid subsequences of length j-1.
                dp[j] = (dp[j] + dp[j-1]) % MOD
    
    # After iterating through all elements, dp[K] will hold the total count
    # of valid subsequences of length K.
    return dp[K]

```