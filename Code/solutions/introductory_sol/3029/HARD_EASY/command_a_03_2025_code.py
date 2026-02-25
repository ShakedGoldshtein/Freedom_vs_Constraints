```python
def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Calculate the Levenshtein distance between two strings.

    The Levenshtein distance is a measure of the minimum number of single-character edits
    (insertions, deletions, or substitutions) required to change one string into the other.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        int: The Levenshtein distance between s1 and s2.
    """
    if s1 == s2:
        return 0

    len_s1 = len(s1)
    len_s2 = len(s2)

    # Initialize a matrix to store the distances between substrings
    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

    # Initialize the base cases
    for i in range(len_s1 + 1):
        dp[i][0] = i
    for j in range(len_s2 + 1):
        dp[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,       # Deletion
                dp[i][j - 1] + 1,       # Insertion
                dp[i - 1][j - 1] + cost # Substitution
            )

    return dp[len_s1][len_s2]
```