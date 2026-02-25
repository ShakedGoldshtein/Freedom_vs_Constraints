```python
from collections import defaultdict

def min_steps_to_anagram(s: str, t: str) -> int:
    """
    Computes the minimum number of character replacements in t to make it an anagram of s.

    Args:
        s: Source string (target anagram).
        t: Target string to modify (must be same length as s).

    Returns:
        The minimum number of replacements needed, or 0 if already an anagram.
    """
    if len(s) != len(t):
        raise ValueError("Input strings must be of equal length")

    def get_char_counts(string: str) -> defaultdict[int]:
        counts = defaultdict(int)
        for char in string:
            counts[char] += 1
        return counts

    s_counts = get_char_counts(s)
    t_counts = get_char_counts(t)

    steps = 0
    for char in s_counts:
        steps += max(0, s_counts[char] - t_counts.get(char, 0))

    return steps
```