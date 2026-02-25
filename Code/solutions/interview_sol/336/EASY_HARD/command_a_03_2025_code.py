```python
from collections import Counter

def minSteps(s: str, t: str) -> int:
    """
    Returns the minimum number of steps to make string t an anagram of string s.
    
    Args:
    s (str): The source string.
    t (str): The target string.
    
    Returns:
    int: The minimum number of steps required.
    """
    # Count the frequency of each character in both strings
    count_s = Counter(s)
    count_t = Counter(t)
    
    # Calculate the difference in character counts between the two strings
    # and sum up the absolute differences
    return sum((count_t - count_s).values())
```