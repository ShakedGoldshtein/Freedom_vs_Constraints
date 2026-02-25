```python
from collections import deque, Counter

def solve(n, a):
    if n == 0:
        return 0
    
    min_val = min(a)
    freq = Counter(a)
    
    queue = deque(a)
    operations = 0
    current_min = min_val
    
    while queue:
        card = queue.popleft()
        operations += 1
        
        if card == current_min:
            freq[card] -= 1
            if freq[card] == 0:
                del freq[card]
                if freq:
                    current_min = min(freq.keys())
                else:
                    break
        else:
            queue.append(card)
    
    return operations
```