```python
def maximize_absolute_sum_pairs(test_cases):
    results = []
    for case in test_cases:
        N, A = case
        A_sorted = sorted(A)
        left = 0
        right = N - 1
        total = 0
        while left < right:
            total += abs(A_sorted[left] - A_sorted[right])
            left += 1
            right -= 1
        results.append(total)
    return results
```