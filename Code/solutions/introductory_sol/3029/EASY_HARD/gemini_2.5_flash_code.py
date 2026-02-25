```python
def levenshtein_distance(s1, s2):
    """
    Calculates the Levenshtein distance between two strings.

    The Levenshtein distance is the minimum number of single-character edits
    (insertions, deletions, or substitutions) required to change one word
    into the other.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        int: The Levenshtein distance between s1 and s2.
    """
    m = len(s1)
    n = len(s2)

    # Create a 2D DP table to store the distances.
    # dp[i][j] will store the Levenshtein distance between s1[:i] and s2[:j].
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the DP table:
    # If s1 is an empty string, the distance to s2[:j] is j (j insertions).
    for j in range(n + 1):
        dp[0][j] = j
    # If s2 is an empty string, the distance to s1[:i] is i (i deletions).
    for i in range(m + 1):
        dp[i][0] = i

    # Fill the DP table using the recurrence relation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate the cost of substitution: 0 if characters are the same, 1 otherwise.
            cost = 0 if s1[i - 1] == s2[j - 1] else 1

            # dp[i][j] is the minimum of three possibilities:
            # 1. Deletion: dp[i-1][j] + 1 (delete s1[i-1])
            # 2. Insertion: dp[i][j-1] + 1 (insert s2[j-1] into s1)
            # 3. Substitution: dp[i-1][j-1] + cost (substitute s1[i-1] with s2[j-1])
            dp[i][j] = min(dp[i - 1][j] + 1,         # Deletion
                           dp[i][j - 1] + 1,         # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution

    # The final result is the distance between the full strings s1 and s2
    return dp[m][n]
```