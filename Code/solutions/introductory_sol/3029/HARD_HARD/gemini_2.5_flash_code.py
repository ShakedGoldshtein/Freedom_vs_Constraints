```python
import collections

def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Calculates the Levenshtein distance between two strings.

    The Levenshtein distance is the minimum number of single-character edits
    (insertions, deletions, or substitutions) required to change one word
    into the other.

    This implementation uses dynamic programming with space optimization,
    achieving O(min(len(s1), len(s2))) space complexity.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        The Levenshtein distance as an integer.

    Raises:
        TypeError: If either s1 or s2 is not a string.

    Time Complexity:
        O(len(s1) * len(s2))
    Space Complexity:
        O(min(len(s1), len(s2)))
    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("Both inputs must be strings.")

    len_s1 = len(s1)
    len_s2 = len(s2)

    # Optimize space by always making s2 the shorter string (or equal length)
    if len_s1 < len_s2:
        s1, s2 = s2, s1
        len_s1, len_s2 = len_s2, len_s1

    # Base case: if one string is empty, the distance is the length of the other
    if len_s2 == 0:
        return len_s1

    # Initialize the 'previous' row of the DP table.
    # dp[0][j] = j corresponds to transforming an empty string to s2[:j]
    # which requires j insertions.
    # prev_row stores distances for s2 up to index j, for s1 up to index i-1.
    prev_row = list(range(len_s2 + 1))

    # Iterate through the longer string (s1)
    for i in range(1, len_s1 + 1):
        # Initialize the 'current' row for dp[i][...]
        # current_row[0] = i corresponds to transforming s1[:i] to an empty string
        # which requires i deletions.
        current_row = [0] * (len_s2 + 1)
        current_row[0] = i

        # Iterate through the shorter string (s2)
        for j in range(1, len_s2 + 1):
            # Cost of substitution: 0 if characters match, 1 otherwise
            substitution_cost = 0 if s1[i-1] == s2[j-1] else 1

            current_row[j] = min(
                prev_row[j] + 1,             # Deletion (from s1[i-1])
                current_row[j-1] + 1,        # Insertion (to match s2[j-1])
                prev_row[j-1] + substitution_cost  # Substitution
            )
        # The current_row becomes the previous_row for the next iteration
        prev_row = current_row

    # The final distance is in the last cell of the last computed row
    return prev_row[len_s2]
```