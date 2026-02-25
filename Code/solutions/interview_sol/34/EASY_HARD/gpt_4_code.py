```python
def max_possible_digits(t, test_cases):
    num_segments = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6]
    results = []
    for i in range(t):
        n = test_cases[i]
        if n % 2 == 0:
            results.append('1' * (n // 2))
        else:
            results.append('7' + '1' * ((n - 3) // 2))
    return results
```