```python
def count_top_card_takes(n, cards):
    position_lists = [[] for _ in range(100001)]
    for i, card in enumerate(cards):
        position_lists[card].append(i+1)
    for list in position_lists:
        list.reverse()
    returned_cards = 0
    current_position = 0
    times_taken = 0
    next_card_positions = []
    for cards_positions in position_lists:
        while cards_positions and (not next_card_positions or next_card_positions[-1] >= cards_positions[-1]):
            while next_card_positions and next_card_positions[-1] < cards_positions[-1]:
                current_position = next_card_positions.pop()
                returned_cards += 1
            current_position = cards_positions.pop()
            times_taken += current_position - returned_cards
            returned_cards += 1
        while cards_positions:
            next_card_positions.append(cards_positions.pop())
    while next_card_positions:
        current_position = next_card_positions.pop()
        times_taken += current_position - returned_cards
        returned_cards += 1
    return times_taken
```