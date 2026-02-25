```python
from collections import deque

def count_card_picks(n, cards):
    dq = deque(cards)
    total_picks = 0
    while dq:
        current_min = min(dq)
        while True:
            card = dq.popleft()
            total_picks += 1
            if card == current_min:
                break
            dq.append(card)
    return total_picks
```