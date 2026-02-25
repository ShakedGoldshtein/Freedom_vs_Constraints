```python
from collections import Counter

def min_steps(s: str, t: str) -> int:
    """
    Calculate the minimum number of steps to make string t an anagram of string s.

    Args:
        s (str): The source string.
        t (str): The target string to be transformed into an anagram of s.

    Returns:
        int: The minimum number of steps required to make t an anagram of s.
    """
    # Count the frequency of each character in both strings
    count_s = Counter(s)
    count_t = Counter(t)

    # Calculate the difference in character counts between s and t
    # The sum of absolute differences gives the minimum number of steps
    return sum((count_t - count_s).values())
```