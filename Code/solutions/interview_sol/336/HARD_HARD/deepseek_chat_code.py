```python
from collections import Counter

def min_steps_to_make_anagram(s, t):
    """
    Calculate the minimum number of character replacements needed to make t an anagram of s.
    
    Args:
        s: Source string
        t: Target string to modify
    
    Returns:
        Minimum number of character replacements needed
    """
    if len(s) != len(t):
        raise ValueError("Strings must be of equal length")
    
    if not s or not t:
        return 0
    
    s_count = Counter(s)
    t_count = Counter(t)
    
    common_chars = 0
    for char in s_count:
        if char in t_count:
            common_chars += min(s_count[char], t_count[char])
    
    return len(s) - common_chars
```