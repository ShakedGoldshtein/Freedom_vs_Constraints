```python
def divide_stones(n, stones):
    total = sum(stones)
    half_size = n // 2
    if n % 2 != 0:
        half_size = (n - 1) // 2

    min_diff = float('inf')
    best_mask = 0

    from itertools import combinations

    for indices in combinations(range(n), half_size):
        current_sum = sum(stones[i] for i in indices)
        current_diff = abs(total - 2 * current_sum)
        if current_diff < min_diff:
            min_diff = current_diff
            best_mask = 0
            for i in indices:
                best_mask |= (1 << i)

    han = []
    chewbacca = []
    for i in range(n):
        if best_mask & (1 << i):
            han.append(stones[i])
        else:
            chewbacca.append(stones[i])

    return (han, chewbacca)
```