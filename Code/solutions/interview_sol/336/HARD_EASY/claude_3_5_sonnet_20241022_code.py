```python
def min_steps_to_anagram(s: str, t: str) -> int:
    """
    Returns minimum steps needed to make t an anagram of s by replacing characters in t.
    
    Args:
        s: Source string
        t: Target string to modify
        
    Returns:
        int: Minimum number of character replacements needed
    """
    if len(s) != len(t):
        return -1
        
    # Count character frequencies in both strings
    char_count_s = {}
    char_count_t = {}
    
    for c in s:
        char_count_s[c] = char_count_s.get(c, 0) + 1
    
    for c in t:
        char_count_t[c] = char_count_t.get(c, 0) + 1
        
    steps = 0
    
    # For each character in s, find how many replacements are needed
    for c in char_count_s:
        count_in_s = char_count_s[c]
        count_in_t = char_count_t.get(c, 0)
        
        # If t has fewer occurrences of c than s, we need to replace characters
        if count_in_t < count_in_s:
            steps += count_in_s - count_in_t
            
    return steps
```