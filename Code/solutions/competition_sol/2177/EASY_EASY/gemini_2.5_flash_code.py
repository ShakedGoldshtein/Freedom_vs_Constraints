```python
import array
from collections import deque

def solve(n, a):
    MAX_CARD_VALUE = 100000

    # Fenwick Tree (Binary Indexed Tree) for efficient range sum queries and point updates
    # to track active cards and their ranks.
    # The Fenwick Tree is 1-indexed internally.
    class FenwickTree:
        def __init__(self, size):
            self.tree = array.array('i', [0] * (size + 1))
            self.size = size
            # Initialize all cards as present
            for i in range(1, size + 1):
                self._update(i, 1)

        # Update the value at index `idx` by `delta`
        def _update(self, idx, delta):
            while idx <= self.size:
                self.tree[idx] += delta
                idx += idx & (-idx)

        # Get the prefix sum up to `idx` (inclusive)
        def query(self, idx):
            s = 0
            while idx > 0:
                s += self.tree[idx]
                idx -= idx & (-idx)
            return s

    # 1. Preprocessing: Count frequencies and store original indices.
    # `counts[value]` stores the number of cards with `value`.
    # `pos_lists[value]` stores a deque of original 0-indexed positions for cards with `value`,
    # in increasing order of their appearance in the input `a`.
    counts = array.array('i', [0] * (MAX_CARD_VALUE + 1))
    pos_lists = [deque() for _ in range(MAX_CARD_VALUE + 1)]
    
    initial_min_val = MAX_CARD_VALUE + 1 # Sentinel for finding true min
    for i, x in enumerate(a):
        counts[x] += 1
        pos_lists[x].append(i)
        if x < initial_min_val:
            initial_min_val = x

    # 2. Initialize Fenwick Tree
    bit = FenwickTree(n)

    # 3. Simulation Variables
    current_min_val = initial_min_val
    total_takes = 0
    cards_present = n
    
    # `current_pos_in_active_cards` is the 0-indexed rank of the card currently at the
    # conceptual 'top' of the deck (among the *active* cards).
    current_pos_in_active_cards = 0

    # 4. Main simulation loop
    while cards_present > 0:
        # Find the next minimum value that is still present in the deck
        while current_min_val <= MAX_CARD_VALUE and counts[current_min_val] == 0:
            current_min_val += 1
        
        # All cards of `current_min_val` are removed in this phase
        # Iterate through the original indices of cards with `current_min_val`
        # in their original deck order.
        for _ in range(len(pos_lists[current_min_val])): # Process all cards of this value
            p_j = pos_lists[current_min_val].popleft() # Original index of the card to remove

            # Find the 0-indexed rank of `p_j` among the currently active cards
            # FenwickTree.query is 1-indexed, so `p_j + 1` is used for original index.
            rank_p_j = bit.query(p_j + 1) - 1

            # Calculate how many cards were "skipped" (moved to the bottom of the deck)
            # to reach `p_j` from `current_pos_in_active_cards`.
            if rank_p_j >= current_pos_in_active_cards:
                # `p_j` is ahead of or at the current top card
                skipped_count = rank_p_j - current_pos_in_active_cards
            else:
                # `p_j` is behind the current top card, requires a full wrap-around
                skipped_count = (cards_present - current_pos_in_active_cards) + rank_p_j
            
            total_takes += skipped_count + 1 # +1 for taking `p_j` itself

            # Remove `p_j` from the deck (conceptually) by updating the Fenwick Tree
            bit._update(p_j + 1, -1)
            cards_present -= 1

            # Update `current_pos_in_active_cards` for the next card to be considered.
            # If `cards_present` is 0, the deck is empty, so `current_pos_in_active_cards`
            # doesn't matter and we can set it to 0.
            # Otherwise, the card that was immediately after `p_j` in the active set
            # now takes its place at rank `rank_p_j`.
            if cards_present > 0:
                current_pos_in_active_cards = rank_p_j % cards_present
            else:
                current_pos_in_active_cards = 0 # Deck is empty

        # All cards of the current minimum value have been removed
        counts[current_min_val] = 0 # Mark this minimum as exhausted
        # `current_min_val` will be incremented in the next iteration of the outer while loop

    return total_takes
```