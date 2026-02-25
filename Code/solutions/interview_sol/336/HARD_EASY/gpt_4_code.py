```python
from collections import Counter

def min_steps_to_make_anagram(s: str, t: str) -> int:
    s_counter = Counter(s)
    t_counter = Counter(t)
    
    diff_count = 0
    for letter, count in s_counter.items():
        if letter not in t_counter or t_counter[letter] < count:
            diff_count += count - t_counter.get(letter, 0)
    return diff_count
```