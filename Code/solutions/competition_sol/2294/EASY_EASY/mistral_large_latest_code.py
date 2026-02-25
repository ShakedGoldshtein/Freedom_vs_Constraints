```python
def solve(N, bags):
    all_numbers = []
    for x, y in bags:
        all_numbers.extend([x, y])
    all_numbers_sorted = sorted(all_numbers)
    min_total = float('inf')

    for i in range(1, 2*N):
        R_max = all_numbers_sorted[-i]
        R_min = all_numbers_sorted[0]
        B_max = all_numbers_sorted[-1]
        B_min = all_numbers_sorted[i]

        current = (R_max - R_min) * (B_max - B_min)
        if current < min_total:
            min_total = current

    return min_total
```