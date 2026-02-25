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
    # Initialize a matrix to store the distances between substrings of s1 and s2
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the base cases:
    # - Transforming an empty string to s2 requires n insertions
    # - Transforming s1 to an empty string requires m deletions
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If the current characters match, there's no edit needed
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                # Otherwise, consider substitution as an edit
                cost = 1

            # Choose the minimum cost among deletion, insertion, and substitution
            dp[i][j] = min(
                dp[i - 1][j] + 1,       # Deletion
                dp[i][j - 1] + 1,       # Insertion
                dp[i - 1][j - 1] + cost # Substitution
            )

    # The Levenshtein distance is found in the bottom-right corner of the matrix
    return dp[m][n]
```