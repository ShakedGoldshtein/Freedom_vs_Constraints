```python
def determine_winner(T, test_cases):
    results = []
    for N in test_cases:
        if N % 4 == 0 or N % 4 == 3:
            results.append('B')
        else:
            results.append('A')
    return results
```