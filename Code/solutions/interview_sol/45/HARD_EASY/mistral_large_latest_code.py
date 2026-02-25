```python
def count_nice_staircases(x):
    def is_nice(n):
        total = n * (n + 1) // 2
        if total > x:
            return False
        remaining = x - total
        if remaining == 0:
            return True
        # Check if remaining can be split into squares
        # The problem reduces to finding if remaining can be expressed as sum of squares <= n
        # We can use a greedy approach to check if remaining can be covered by squares
        # The largest possible square is min(n, sqrt(remaining))
        max_square = int(remaining ** 0.5)
        if max_square > n:
            max_square = n
        # Try to cover remaining with squares <= max_square
        # We can use a BFS or DP approach, but for large x, we need a smarter method
        # Here, we use a greedy approach: take the largest possible square first
        current = remaining
        while current > 0:
            s = int(current ** 0.5)
            if s > max_square:
                s = max_square
            if s == 0:
                return False
            current -= s * s
            max_square = s - 1
        return True

    max_n = int((2 * x) ** 0.5) + 2
    count = 0
    for n in range(1, max_n + 1):
        if is_nice(n):
            count += 1
    return count

def solve(t, test_cases):
    results = []
    for x in test_cases:
        results.append(count_nice_staircases(x))
    return results
```