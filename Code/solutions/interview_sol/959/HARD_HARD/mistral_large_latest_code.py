```python
def maximize_absolute_pair_sum(test_cases):
    results = []
    for case in test_cases:
        n, arr = case
        arr_sorted = sorted(arr)
        left = 0
        right = n - 1
        total = 0
        while left < right:
            total += abs(arr_sorted[left] - arr_sorted[right])
            left += 1
            right -= 1
        results.append(total)
    return results

def solve(t, cases):
    test_cases = []
    for i in range(t):
        n, arr = cases[i]
        test_cases.append((n, arr))
    return maximize_absolute_pair_sum(test_cases)
```