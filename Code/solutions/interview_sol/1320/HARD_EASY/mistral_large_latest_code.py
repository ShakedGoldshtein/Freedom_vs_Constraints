```python
def determine_winner(test_cases):
    results = []
    for n in test_cases:
        if n == 1 or n % 4 in (0, 3):
            results.append('B')
        else:
            results.append('A')
    return results
```