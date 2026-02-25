```python
from collections import deque

def count_top_card_picks(n, cards):
    """
    Counts the total number of times the top card is picked from the deck during Vasily's sorting process.

    Args:
        n: Number of cards in the deck.
        cards: List of integers representing the card values from top to bottom.

    Returns:
        int: Total number of times the top card is picked.
    """
    if n == 0:
        return 0

    deck = deque(cards)
    operations = 0
    current_min = min(deck)

    while deck:
        card = deck.popleft()
        operations += 1

        if card == current_min:
            # Remove all instances of current_min from the deck
            while deck and deck[0] == current_min:
                deck.popleft()
                operations += 1

            # Update current_min if deck is not empty
            if deck:
                current_min = min(deck)
        else:
            deck.append(card)

    return operations
```