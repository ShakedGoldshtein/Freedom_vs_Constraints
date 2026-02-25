```python
from collections import defaultdict

def min_steps_to_anagram(s: str, t: str) -> int:
    freq = defaultdict(int)
    for c in s:
        freq[c] += 1
    for c in t:
        freq[c] -= 1
    return sum(abs(v) for v in freq.values()) // 2
```