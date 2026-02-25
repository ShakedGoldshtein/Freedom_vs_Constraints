```python
import collections
import bisect

class FenwickTree:
    """
    A Fenwick Tree (Binary Indexed Tree) for efficient prefix sum queries
    and single-point updates on a 0-indexed array.
    """
    def __init__(self, size: int):
        """
        Initializes the Fenwick Tree with a given size.
        All elements are initially zero.

        Args:
            size: The size of the array the Fenwick Tree represents.
        """
        self._size = size
        self._bit = [0] * (size + 1) # Internal array is 1-indexed

    def update(self, idx: int, delta: int):
        """
        Adds `delta` to the element at `idx`.
        
        Args:
            idx: The 0-indexed position to update.
            delta: The value to add to the element at `idx`.
        """
        idx += 1 # Convert to 1-indexed
        while idx <= self._size:
            self._bit[idx] += delta
            idx += idx & (-idx)

    def query(self, idx: int) -> int:
        """
        Returns the prefix sum of elements from index 0 up to `idx` (inclusive).
        
        Args:
            idx: The 0-indexed upper bound of the sum.
        
        Returns:
            The sum of elements in the range [0, idx].
        """
        if idx < 0:
            return 0
        idx += 1 # Convert to 1-indexed
        res = 0
        while idx > 0:
            res += self._bit[idx]
            idx -= idx & (-idx)
        return res

    def query_range(self, start: int, end: int) -> int:
        """
        Returns the sum of elements in the range [start, end] (inclusive).
        
        Args:
            start: The 0-indexed lower bound of the range.
            end: The 0-indexed upper bound of the range.
            
        Returns:
            The sum of elements in the range [start, end].
            Returns 0 if start > end (empty range).
        """
        if start > end:
            return 0
        return self.query(end) - self.query(start - 1)

def solve(n: int, cards: list[int]) -> int:
    """
    Calculates the total number of times Vasily takes a card from the deck
    to sort it according to the specified rules.

    The process involves repeatedly taking the top card. If it's the minimum
    among remaining cards, it's placed away. Otherwise, it's put under the deck.
    This continues until the deck is empty.

    Args:
        n: The number of cards in the deck.
        cards: A list of integers representing the numbers on the cards,
               from top to bottom.

    Returns:
        The total number of times Vasily takes a card from the deck.
    """
    # Input validation based on problem constraints.
    if not (1 <= n <= 100000):
        raise ValueError("n must be between 1 and 100,000.")
    if len(cards) != n:
        raise ValueError("Length of 'cards' list must match 'n'.")

    max_card_value = 0
    card_locations = collections.defaultdict(list)
    for i, card_val in enumerate(cards):
        if not (1 <= card_val <= 100000):
            raise ValueError("Card values must be between 1 and 100,000.")
        card_locations[card_val].append(i)
        if card_val > max_card_value:
            max_card_value = card_val

    # Initialize Fenwick Tree to keep track of active (not yet removed) cards.
    # A value of 1 at an index means the card at that original position is still in the deck.
    # A value of 0 means it has been removed.
    bit = FenwickTree(n)
    for i in range(n):
        bit.update(i, 1) # All cards are initially present

    total_takes = 0
    # last_removed_idx stores the original index of the last card removed in the *previous* round.
    # It defines the "effective start" of the cyclic deck for the current round.
    # E.g., if last_removed_idx = 3, the deck conceptually starts at original index 4,
    # wraps around to 0, and ends at 3.
    last_removed_idx = -1

    # Vasily removes cards in increasing order of their values.
    # We iterate through possible card values from 1 up to the maximum observed value.
    for current_min_val in range(1, max_card_value + 1):
        m_indices = card_locations[current_min_val]
        if not m_indices:
            continue # No cards with this value in the deck

        # Determine which 'current_min_val' cards are "before" last_removed_idx
        # in the original array order, and which are "after".
        # Cards after last_removed_idx are processed first in a cyclic scan.
        # bisect_right finds the insertion point for last_removed_idx,
        # effectively splitting m_indices into two logical parts for the cyclic deck.
        split_point = bisect.bisect_right(m_indices, last_removed_idx)
        
        # These are cards whose original index is > last_removed_idx.
        # They appear in the first segment of the cyclic scan (from last_removed_idx + 1 to n-1).
        indices_in_first_segment = m_indices[split_point:]
        
        # These are cards whose original index is <= last_removed_idx.
        # They appear in the second segment of the cyclic scan (wrap-around from 0 to last_removed_idx).
        indices_in_second_segment = m_indices[:split_point]

        # Process cards in the first segment
        # (from original index `last_removed_idx + 1` up to `n-1`)
        if indices_in_first_segment:
            # Cost to scan past cards (not current_min_val) before the first m in this segment.
            # `last_removed_idx + 1` correctly handles cases where `last_removed_idx` is -1 (start from 0).
            cost_to_reach_first_m = bit.query_range(last_removed_idx + 1, indices_in_first_segment[0] - 1)
            total_takes += cost_to_reach_first_m
            
            # Cost to take all 'm' cards in this segment. Each take increments the count by 1.
            total_takes += len(indices_in_first_segment)
            last_removed_idx = indices_in_first_segment[-1] # Update last_removed_idx

        # Process cards in the second segment (if any, meaning a wrap-around occurred)
        # (from original index `0` up to `last_removed_idx`)
        if indices_in_second_segment:
            # Cards from the current `last_removed_idx + 1` (after processing first segment, or from previous `m` round)
            # to the end of the original array (`n-1`) must be scanned and rotated to reach
            # the beginning of the original array (`0`) where `indices_in_second_segment` start.
            cost_to_wrap_around = bit.query_range(last_removed_idx + 1, n - 1)
            total_takes += cost_to_wrap_around
            
            # Now, effectively we are scanning from original index 0.
            # Cost to scan past cards (not current_min_val) before the first m in this wrapped-around segment.
            cost_to_reach_first_m_wrapped = bit.query_range(0, indices_in_second_segment[0] - 1)
            total_takes += cost_to_reach_first_m_wrapped

            # Cost to take all 'm' cards in this wrapped-around segment.
            total_takes += len(indices_in_second_segment)
            last_removed_idx = indices_in_second_segment[-1] # Update last_removed_idx to the last one removed

        # After calculating costs, mark all instances of current_min_val as removed in the Fenwick Tree.
        # This updates future `query_range` calls to reflect fewer active cards.
        for idx in m_indices:
            bit.update(idx, -1)

    return total_takes
```