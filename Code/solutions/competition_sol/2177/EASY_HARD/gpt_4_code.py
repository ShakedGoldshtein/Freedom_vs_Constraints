```python
from collections import deque, defaultdict
    
def total_card_takes(n, cards):
    card_locations = defaultdict(deque)
    for i in range(n):
        card_locations[cards[i]].append(i)
    for k in card_locations.keys():
        card_locations[k] = deque(sorted(card_locations[k]))

    sorted_cards = sorted(card_locations.keys())
    total_takes = idx = 0
    for card in sorted_cards:
        while card_locations[card]:
            if card_locations[card][0] >= idx:
                idx = card_locations[card].popleft()
                total_takes += 1
            else:
                card_locations[card].append(card_locations[card].popleft())
                total_takes += 1
    return total_takes
```