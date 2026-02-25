```python
import collections

def count_manhattan_euclidean_pairs(n: int, watchmen_coordinates: list[tuple[int, int]]) -> int:
    """
    Calculates the number of pairs of watchmen (i, j) with i < j such that
    the Manhattan distance between them is equal to the Euclidean distance.

    The condition for this equality ( |x1 - x2| + |y1 - y2| = sqrt((x1 - x2)^2 + (y1 - y2)^2) )
    simplifies to either |x1 - x2| = 0 or |y1 - y2| = 0.
    This means the two watchmen must lie on the same horizontal line (same y-coordinate)
    or on the same vertical line (same x-coordinate).

    The total number of such pairs can be found using the Principle of Inclusion-Exclusion:
    Count(pairs with same x) + Count(pairs with same y) - Count(pairs with same (x, y)).

    Args:
        n: The total number of watchmen. This parameter is used for type hinting/documentation
           and implies `len(watchmen_coordinates)` should equal `n`.
           (Constraint: 1 <= n <= 200,000)
        watchmen_coordinates: A list of tuples, where each tuple (x_i, y_i)
                              represents the coordinates of a watchman.
                              (Constraint: |x_i|, |y_i| <= 10^9)

    Returns:
        The total number of pairs of watchmen satisfying the condition.

    Time Complexity: O(N), where N is the number of watchmen.
                     This involves a single pass to populate frequency maps and
                     then iterating through the unique keys in these maps.
                     Dictionary operations (insertion, lookup) are O(1) on average.
    Space Complexity: O(N), where N is the number of watchmen.
                      In the worst case, all x-coordinates, y-coordinates, and
                      (x,y) pairs could be unique, requiring space proportional to N
                      for the frequency maps.
    """
    if n <= 1:
        return 0

    # Dictionaries to store frequency counts of x-coordinates, y-coordinates,
    # and (x, y) coordinate pairs.
    # collections.defaultdict(int) automatically initializes new keys with a default value of 0.
    x_counts = collections.defaultdict(int)
    y_counts = collections.defaultdict(int)
    xy_counts = collections.defaultdict(int)

    # Populate the frequency counts by iterating through all watchmen coordinates.
    for x, y in watchmen_coordinates:
        x_counts[x] += 1
        y_counts[y] += 1
        xy_counts[(x, y)] += 1

    total_satisfying_pairs = 0

    def calculate_pairs_from_frequency(count: int) -> int:
        """
        Calculates the number of unique pairs (i, j) with i < j
        that can be formed from 'count' items.
        Formula: k * (k - 1) / 2
        """
        if count < 2:
            return 0
        return count * (count - 1) // 2

    # 1. Add pairs that share the same x-coordinate (on a vertical line).
    # Each group of 'count' watchmen with the same x-coordinate contributes
    # calculate_pairs_from_frequency(count) to the total.
    for count in x_counts.values():
        total_satisfying_pairs += calculate_pairs_from_frequency(count)

    # 2. Add pairs that share the same y-coordinate (on a horizontal line).
    # Each group of 'count' watchmen with the same y-coordinate contributes
    # calculate_pairs_from_frequency(count) to the total.
    for count in y_counts.values():
        total_satisfying_pairs += calculate_pairs_from_frequency(count)

    # 3. Subtract pairs that share both the same x and y coordinates (identical points).
    # These pairs were double-counted in steps 1 and 2 (once for same x, once for same y).
    # We apply the Principle of Inclusion-Exclusion by subtracting them once.
    for count in xy_counts.values():
        total_satisfying_pairs -= calculate_pairs_from_frequency(count)

    return total_satisfying_pairs
```