```python
from collections import Counter

def solve(T, test_cases):
    for _ in range(T):
        N, colors = test_cases[_]
        color_counts = Counter(colors)

        # Check if the max frequency is more than half the total. If yes, conflict can't be resolved
        if max(color_counts.values()) > (N + 1) // 2:
            yield "No"
        else:
            sorted_colors = sorted(colors)
            mid = N // 2
            sorted_colors[mid:], sorted_colors[:mid] = sorted_colors[:mid], sorted_colors[mid:]
            yield "Yes"
            yield sorted_colors
            
# For testing the function

test_cases = [
    (9, [1, 1, 1, 2, 2, 2, 3, 3, 3]),
    (2, [1, 1])
]

for result in solve(2, test_cases):
    print(result)
```