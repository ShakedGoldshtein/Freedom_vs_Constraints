```python
import collections

def solve(n, points):
    x_counts = collections.defaultdict(int)
    y_counts = collections.defaultdict(int)
    xy_counts = collections.defaultdict(int)

    for x, y in points:
        x_counts[x] += 1
        y_counts[y] += 1
        xy_counts[(x, y)] += 1

    total_matching_pairs = 0

    def combinations_2(count):
        if count < 2:
            return 0
        return count * (count - 1) // 2

    for count in x_counts.values():
        total_matching_pairs += combinations_2(count)

    for count in y_counts.values():
        total_matching_pairs += combinations_2(count)

    for count in xy_counts.values():
        total_matching_pairs -= combinations_2(count)

    return total_matching_pairs
```